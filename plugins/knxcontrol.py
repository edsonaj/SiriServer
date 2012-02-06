#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class knxcontrol(Plugin):
    
##OFICE
    
    @register("en-US", "(.*escritório.*ligar.*)|(.*ligar.*escritório.*)|(.*escritorio.*ligue.*)|(.*ligue.*escritorio.*)")
    def st_officeon(self, speech, language):
        self.say ("Ligando as luzes do escritorio.","Turning on the office lights") 
    	os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_ON.jar'")
    	self.complete_request()
  
    @register("en-US", "(.*escritorio.*desligar.*)|(.*desligar.*escritorio.*)|(.*escritorio.*desligue.*)|(.*desligue.*escritorio.*)")
    def st_officeoff(self, speech, language):
    	self.say ("Desligando as luzes do escritorio.","Turning off the office lights") 
    	os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_OFF.jar'")
    	self.complete_request()

##KITCHEN
    
    @register("en-US", "(.*cozinha.*ligar.*)|(.*ligar.*cozinha.*)|(.*cozinha.*ligue.*)|(.*ligue.*cozinha.*)")
    def st_kitchenon(self, speech, language):
        self.say ("Ligando as luzes da cozinha.","Turning on kitchen lights") 
        system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_1.jar'")
        self.system ("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_2.jar'")
        self.complete_request()
    
    @register("en-US", "(.*cozinha.*desligar.*)|(.*desligar.*cozinha.*)|(.*cozinha.*desligue.*)|(.*desligue.*cozinha.*)")
    def st_kitchenoff(self, speech, language):
        self.say ("Desligando as luzes da cozinha.","Turning off kitchen lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_2.jar'")
        self.complete_request()