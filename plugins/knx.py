#Siri Server plugin - SiriServer KNX Plugin (Calimero API 1.4)
#Portuguese plugin for use with this fork: https://github.com/edsonaj/SiriServer


from plugin import *

class knx(Plugin):
    
##OFICE
    
    @register("en-US", "(.*escritório.*ligar.*)|(.*ligar.*escritório.*)")
        def st_hello(self, speech, language):
        self.say ("Ligando as luzes do escritório.","Turning on the office lights") 
    	system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_ON.jar'")
    	self.complete_request()
  
    @register("en-US", "(.*escritório.*desligar.*)|(.*desligar.*escritório.*)")
        def st_hello(self, speech, language):
    	self.say ("Desligando as luzes do escritório.","Turning off the office lights") 
    	system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_OFF.jar'")
    	self.complete_request()

##KITCHEN
    
    @register("en-US", "(.*cozinha.*ligar.*)|(.*ligar.*cozinha.*)")
        def st_hello(self, speech, language):
        self.say ("Ligando as luzes da cozinha.","Turning on kitchen lights") 
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_1.jar'")
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_2.jar'")
        self.complete_request()
    
    @register("en-US", "(.*cozinha.*desligar.*)|(.*desligar.*cozinha.*)")
        def st_hello(self, speech, language):
        self.say ("Desligando as luzes da cozinha.","Turning off kitchen lights")
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_1.jar'")
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_2.jar'")
        self.complete_request()