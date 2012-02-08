#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class sala(Plugin):
    
    @register("pt-BR", ".*ligar.*sala.*")
    def st_roomon(self, speech, language):
        resp1 = self.ask("Direta ou Indireta?")
        if resp1 == "Direta":
            self.say("Ligando as luzes da sala.","Turning on living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_1.jar'")
        else if resp1 == "Indireta":
            self.say("Ligando as luzes da sala.","Turning on living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_2.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_3.jar'")
        else:
        	self.say("Desculpe, nao entendi.","Sorry, I didn't get that.")
    	self.complete_request()

    @register("pt-BR", ".*desligar.*sala.*")
    def st_roomoff(self, speech, language):
        resp2 = self.ask("Direta ou Indireta?")
        if resp2 == "Direta":
            self.say("Desligando as luzes da sala.","Turning off living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_1.jar'")
        else if resp2 == "Indireta":
            self.say("Desligando as luzes da sala.","Turning off living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_2.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_3.jar'")
        else:
        	self.say("Desculpe, nao entendi.","Sorry, I didn't get that.")	
	self.complete_request()