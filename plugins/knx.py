#Siri Server plugin - SiriServer KNX Plugin (Calimero API 1.4)
#Portuguese plugin

from plugin import *

class knx(Plugin):
    
##OFICE
    
    @register("en-US", "(.*escritorio.*ligar.*)|(.*ligar.*escritorio.*)|(.*escritorio.*ligue.*)|(.*ligue.*escritorio.*)")
        def st_office_on(self, speech, language):
        self.say ("Ligando as luzes do escritório.","Turning on the office lights") 
    	system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_ON.jar'")
    	self.complete_request()
  
    @register("en-US", "(.*escritorio.*desligar.*)|(.*desligar.*escritorio.*)|(.*escritorio.*desligue.*)|(.*desligue.*escritorio.*)")
        def st_office_off(self, speech, language):
    	self.say ("Desligando as luzes do escritorio.","Turning off the office lights") 
    	system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_OFF.jar'")
    	self.complete_request()

##KITCHEN
    
    @register("en-US", "(.*cozinha.*ligar.*)|(.*ligar.*cozinha.*)|(.*cozinha.*ligue.*)|(.*ligue.*cozinha.*)")
        def st_kitchen_on(self, speech, language):
        self.say ("Ligando as luzes da cozinha.","Turning on kitchen lights") 
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_1.jar'")
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_2.jar'")
        self.complete_request()
    
    @register("en-US", "(.*cozinha.*desligar.*)|(.*desligar.*cozinha.*)|(.*cozinha.*desligue.*)|(.*desligue.*cozinha.*)")
        def st_kitchen_off(self, speech, language):
        self.say ("Desligando as luzes da cozinha.","Turning off kitchen lights")
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_1.jar'")
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_2.jar'")
        self.complete_request()