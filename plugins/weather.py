#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Sebastian Koch

import re
import urllib2, urllib, uuid
import json
import random


from plugin import *
from datetime import date
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.forecastObjects import *

#Obtain API Key from wundergrounds.com
weatherApiKey ="37e4db47f3466bfb"

class SiriWeatherFunctions():
    def __init__(self):
        self.conditionTerm="clear"
        self.night=False
        self.result=dict()
    def __missing__(self, key): 
        result = self[key] = D() 
        return result 
    
    def swapCondition(self,conditionTerm="clear", night=False):
        conditionsArray={"cloudy":{"conditionCodeIndex":26,"conditionCode":"Cloudy","night":{"conditionCodeIndex":27,"conditionCode":"MostlyCloudyNight"}},"rain":{"conditionCodeIndex":11,"conditionCode":"Showers"},"unknown":{"conditionCodeIndex":26,"conditionCode":"Cloudy"},"partlycloudy":{"conditionCodeIndex":30,"conditionCode":"PartlyCloudyDay","night":{"conditionCodeIndex":29,"conditionCode":"PartlyCloudyNight"}},"tstorms":{"conditionCodeIndex":4,"conditionCode":"Thunderstorms"},"sunny":{"conditionCodeIndex":32,"conditionCode":"Sunny","night":{"conditionCodeIndex":31,"conditionCode":"ClearNight"}},"snow":{"conditionCodeIndex":16,"conditionCode":"Snow"},"sleet":{"conditionCodeIndex":18,"conditionCode":"Sleet"},"partlysunny":{"conditionCodeIndex":30,"conditionCode":"PartlyCloudyDay","night":{"conditionCodeIndex":29,"conditionCode":"PartlyCloudyNight"}},"mostlysunny":{"conditionCodeIndex":34,"conditionCode":"FairDay","night":{"conditionCodeIndex":33,"conditionCode":"FairNight"}},"mostlycloudy":{"conditionCodeIndex":28,"conditionCode":"MostlyCloudyDay","night":{"conditionCodeIndex":27,"conditionCode":"MostlyCloudyNight"}},"hazy":{"conditionCodeIndex":21,"conditionCode":"Haze","night":{"conditionCodeIndex":29,"conditionCode":"PartlyCloudyNight"}},"fog":{"conditionCodeIndex":20,"conditionCode":"Foggy"},"flurries":{"conditionCodeIndex":13,"conditionCode":"SnowFlurries"},"clear":{"conditionCodeIndex":32,"conditionCode":"Sunny","night":{"conditionCodeIndex":31,"conditionCode":"ClearNight"}},"chancetstorms":{"conditionCodeIndex":38,"conditionCode":"ScatteredThunderstorms"},"chancesnow":{"conditionCodeIndex":42,"conditionCode":"ScatteredSnowShowers"},"chancesleet":{"conditionCodeIndex":6,"conditionCode":"MixedRainAndSleet"},"chancerain":{"conditionCodeIndex":40,"conditionCode":"ScatteredShowers"},"chanceflurries":{"conditionCodeIndex":13,"conditionCode":"SnowFlurries"}}
        self.conditionTerm=conditionTerm.replace("nt_","")
        self.night = night
        
        if (conditionsArray[self.conditionTerm].has_key("night")) and (self.night==True):
            self.result["conditionCode"]=conditionsArray[self.conditionTerm]["night"]["conditionCode"]
            self.result["conditionCodeIndex"]=conditionsArray[self.conditionTerm]["night"]["conditionCodeIndex"]
        else:
            self.result["conditionCode"]=conditionsArray[self.conditionTerm]["conditionCode"]
            self.result["conditionCodeIndex"]=conditionsArray[self.conditionTerm]["conditionCodeIndex"]        
        
        return self.result



class weatherPlugin(Plugin):
    localizations = {"weatherForecast": 
                        {"search":{
                            0:{"pt-BR": "Checando minhas fontes..."},
                            1:{"pt-BR": "Por favor espere enquanto checo..."},
                            2:{"pt-BR": "Um momento por favor..."},
                            3:{"pt-BR": "Tentando obter a previsao..."},
                            }, 
                        "forecast":{
                            "DAILY": {
                                0:{"pt-BR": "O tempo hoje em {0}, {1} e"},
                                1:{"pt-BR": "Este e a previsao para {0}, {1}"},
                                2:{"pt-BR": "Eu achei a seguinte informacao sobre o tempo para {0}, {1}"},
                                },
                            "HOURLY": {
                                0:{"pt-BR": "O tempo hoje em {0}, {1} e"},
                                1:{"pt-BR": "Este e a previsao para {0}, {1}"},
                                2:{"pt-BR": "Eu achei a seguinte informacao sobre o tempo para {0}, {1}"},
                                }
                            },
                        "failure": {
                                   "pt-BR": "Me desculpe, mais nao acho a previsao para esta localidade!"
                                   }
                            }
                        }
            
    @register("pt-BR", "(.*Previsão.*Tempo.*)|(.*Tempo.*)")
    def weatherForecastLookUp(self, speech, language):
        if weatherApiKey =="":
            self.say("Por favor obtenha a chave API em http://api.wunderground.com/weather/api/ e coloque-a na linha 17!")
            self.complete_Request()
            pass
        viewType ="DAILY"
        if (speech.count("hoje") > 0 or speech.count("agora") > 0 or speech.count("para hoje") > 0):
            viewType = "HOURLY"
            speech = speech.replace("hoje","")
            speech = speech.replace("agora","")
            speech = speech.replace("neste momento","")
            speech = speech.replace(" para "," in ")
        
        if language=="pt-BR":
            speech = speech.replace(" para "," in ")
            

                
        error = False
        view = AddViews(refId=self.refId, dialogPhase="Reflection")
        print weatherPlugin.localizations
        randomNumber = random.randint(0,3)
        view.views = [AssistantUtteranceView(weatherPlugin.localizations['weatherForecast']['search'][randomNumber]["pt-BR"], weatherPlugin.localizations['weatherForecast']['search'][randomNumber]["pt-BR"])]
        self.connection.send_object(view)
        
        

        
                
        
        countryOrCity = re.match("(?u).*em ([\w ]+)", speech, re.IGNORECASE)
        if countryOrCity != None:
            countryOrCity = countryOrCity.group(1).strip()
            print "found forecast"
            # lets see what we got, a country or a city... 
            # lets use google geocoding API for that
            url = "http://maps.googleapis.com/maps/api/geocode/json?address={0}&sensor=false&language={1}".format(urllib.quote_plus(countryOrCity.encode("utf-8")), "pt-BR")
        elif countryOrCity == None:
            currentLocation=self.getCurrentLocation()
            url = "http://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&sensor=false&language={2}".format(str(currentLocation.latitude),str(currentLocation.longitude), "pt-BR")
           
            # lets wait max 3 seconds
        jsonString = None
        try:
            jsonString = urllib2.urlopen(url, timeout=3).read()
        except:
            pass
        if jsonString != None:
            response = json.loads(jsonString)
            # lets see what we have...
            if response['status'] == 'OK':
                components = response['results'][0]['address_components']
                types = components[0]['types'] # <- this should be the city or country
                if "country" in types:
                    # OK we have a country as input, that sucks, we need the capital, lets try again and ask for capital also
                    components = filter(lambda x: True if "country" in x['types'] else False, components)
                    url = "http://maps.googleapis.com/maps/api/geocode/json?address=capital%20{0}&sensor=false&language={1}".format(urllib.quote_plus(components[0]['long_name']), "pt-BR")
                        # lets wait max 3 seconds
                    jsonString = None
                    try:
                        jsonString = urllib2.urlopen(url, timeout=3).read()
                    except:
                        pass
                    if jsonString != None:
                        response = json.loads(jsonString)
                        if response['status'] == 'OK':
                            components = response['results'][0]['address_components']
            # response could have changed, lets check again, but it should be a city by now 
            if response['status'] == 'OK':
                # get latitude and longitude
                location = response['results'][0]['geometry']['location']
                
                
                city = filter(lambda x: True if "locality" in x['types'] or "administrative_area_level_1" in x['types'] else False, components)[0]['long_name']
                country = filter(lambda x: True if "country" in x['types'] else False, components)[0]['long_name']
                state = filter(lambda x: True if "administrative_area_level_1" in x['types'] or "country" in x['types'] else False, components)[0]['short_name']
                stateLong = filter(lambda x: True if "administrative_area_level_1" in x['types'] or "country" in x['types'] else False, components)[0]['long_name']
                countryCode = filter(lambda x: True if "country" in x['types'] else False, components)[0]['short_name']
                url = "http://api.wunderground.com/api/{0}/geolookup/conditions/forecast7day//hourly7day/astronomy/q/{1},{2}.json".format(weatherApiKey, location['lat'], location['lng'])
                 # lets wait max 3 seconds
                jsonString = None
                try:
                    jsonString = urllib2.urlopen(url, timeout=5).read()
                except:
                    pass
                if jsonString != None:
                    response = json.loads(jsonString)
                    # lets see what we have...
                    if response.has_key("error")==False:
                        weatherTemp=dict()
                        if response.has_key("current_observation"):
                            if response.has_key("moon_phase"):
                                if (int(response["moon_phase"]["current_time"]["hour"]) > int(response["moon_phase"]["sunset"]["hour"])) or (int(response["moon_phase"]["current_time"]["hour"]) < int(response["moon_phase"]["sunrise"]["hour"])):
                                    weatherTempNightTime = True
                                    
                                else:
                                   weatherTempNightTime = False
                            else:
                                weatherTempNightTime = False
                                
                            conditionSwapper = SiriWeatherFunctions()
                            
                            dayOfWeek=dict()
                            dayOfWeek[0]=2
                            dayOfWeek[1]=3
                            dayOfWeek[2]=4
                            dayOfWeek[3]=5
                            dayOfWeek[4]=6
                            dayOfWeek[5]=7
                            dayOfWeek[6]=1
                            
                            tempNight=weatherTempNightTime
                            weatherTemp["currentTemperature"] =str(response["current_observation"]["temp_c"])
                            dailyForecasts=[]
                            for x in range(0,6):
                                forecastDate = date(int(response["forecast"]["simpleforecast"]["forecastday"][x]["date"]["year"]),int(response["forecast"]["simpleforecast"]["forecastday"][x]["date"]["month"]),int(response["forecast"]["simpleforecast"]["forecastday"][x]["date"]["day"]))
                                
                                weatherTemp["tempCondition"] = conditionSwapper.swapCondition(conditionTerm=response["forecast"]["simpleforecast"]["forecastday"][x]["icon"], night=tempNight)
                                dailyForecasts.append(SiriForecastAceWeathersDailyForecast(timeIndex=(dayOfWeek[date.weekday(forecastDate)]), highTemperature=response["forecast"]["simpleforecast"]["forecastday"][x]["high"]["celsius"], lowTemperature=response["forecast"]["simpleforecast"]["forecastday"][x]["low"]["celsius"], condition=SiriForecastAceWeathersConditions(conditionCode=weatherTemp["tempCondition"]["conditionCode"], conditionCodeIndex=weatherTemp["tempCondition"]["conditionCodeIndex"])))
                                tempNight=False
                               
                            hourlyForecasts=[]
                            for x in range(0,10):
                                if response["hourly_forecast"][x]:
                                    if (int(response["moon_phase"]["current_time"]["hour"]) <= int(response["hourly_forecast"][x]["FCTTIME"]["hour"])) or (int(response["forecast"]["simpleforecast"]["forecastday"][0]["date"]["day"]) < int(response["hourly_forecast"][x]["FCTTIME"]["mday"])) or (int(response["forecast"]["simpleforecast"]["forecastday"][0]["date"]["month"]) < int(response["hourly_forecast"][x]["FCTTIME"]["mon"])):
                                        if response.has_key("hourly_forecast")==True:
                                            weatherTemp=dict()
                                            if response.has_key("current_observation"):
                                                if response.has_key("moon_phase"):
                                                    if (int(response["moon_phase"]["sunset"]["hour"]) < int(response["hourly_forecast"][x]["FCTTIME"]["hour"])) or (int(response["moon_phase"]["sunrise"]["hour"]) > int(response["hourly_forecast"][x]["FCTTIME"]["hour"])):
                                                         weatherTempCon = conditionSwapper.swapCondition(conditionTerm=response["hourly_forecast"][x]["icon"], night=True)
                                       
                                                        
                                                    else:
                                                       weatherTempCon = conditionSwapper.swapCondition(conditionTerm=response["hourly_forecast"][x]["icon"], night=False)
                                       
                                                else:
                                                    weatherTempCon = conditionSwapper.swapCondition(conditionTerm=response["hourly_forecast"][x]["icon"], night=True)
                                       
                                    
                                        hourlyForecasts.append(SiriForecastAceWeathersHourlyForecast(timeIndex=response["hourly_forecast"][x]["FCTTIME"]["hour"], chanceOfPrecipitation=int(response["hourly_forecast"][x]["pop"]), temperature=response["hourly_forecast"][x]["temp"]["metric"],  condition=SiriForecastAceWeathersConditions(conditionCode=weatherTempCon["conditionCode"], conditionCodeIndex=weatherTempCon["conditionCodeIndex"])))
                                        
                            weatherTemp["currentCondition"] = conditionSwapper.swapCondition(conditionTerm=response["current_observation"]["icon"], night=weatherTempNightTime)
                            currentTemperature=str(response["current_observation"]["temp_c"])
                            currentDate=date(int(response["forecast"]["simpleforecast"]["forecastday"][0]["date"]["year"]),int(response["forecast"]["simpleforecast"]["forecastday"][0]["date"]["month"]),int(response["forecast"]["simpleforecast"]["forecastday"][0]["date"]["day"]))
                            view = AddViews(self.refId, dialogPhase="Summary")
                            
                            currentConditions=SiriForecastAceWeathersCurrentConditions(dayOfWeek=dayOfWeek[int(date.weekday(currentDate))],temperature=currentTemperature, condition=SiriForecastAceWeathersConditions(conditionCode=weatherTemp["currentCondition"]["conditionCode"], conditionCodeIndex=weatherTemp["currentCondition"]["conditionCodeIndex"]))
                            
                            aceWethers=[SiriForecastAceWeathers(extendedForecastUrl = response["location"]["wuiurl"], currentConditions=currentConditions, hourlyForecasts=hourlyForecasts, dailyForecasts=dailyForecasts, weatherLocation=SiriForecastAceWeathersWeatherLocation(), units=SiriForecastAceWeathersUnits(), view=viewType, )]
                            weather = SiriForecastSnippet(aceWeathers=aceWethers)
                            speakCountry = stateLong if country == "United States" else country
                            randomNumber = random.randint(0,2)
                            view.views = [AssistantUtteranceView(text=weatherPlugin.localizations['weatherForecast']['forecast'][viewType][randomNumber]["pt-BR"].format(city, speakCountry),speakableText=weatherPlugin.localizations['weatherForecast']['forecast'][viewType][randomNumber]["pt-BR"].format(city,speakCountry), dialogIdentifier="Weather#forecastCommentary"), weather]
                            self.sendRequestWithoutAnswer(view)
                        else:
                            error = True
                    else:
                        error = True
                else:
                    error = True
            else:
                error = True
        else:
            error = True
                           
                         
                                    
        if error:                           
            self.say(weatherPlugin.localizations['weatherForecast']['failure']["pt-BR"])
        self.complete_request()