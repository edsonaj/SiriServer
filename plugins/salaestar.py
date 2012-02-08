#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class salacontrol(Plugin):
    
    @register("pt-BR", ".*ligar.*sala.*")
    def st_room_on(self, speech, language):
        resposta = self.ask(u"Direta ou Indireta?")
        if resposta == "Direta":
        	self.say("{0}","")
            self.say("Ligando as luzes da sala.","Turning on living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_1.jar'")
        else if resposta == "Indireta":
        	self.say("{0}","")
            self.say("Ligando as luzes da sala.","Turning on living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_2.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_3.jar'")
        else:
        	self.say("{0}","")
        	self.say("Desculpe, nao entendi.","Sorry, I didn't get that.")
    	self.complete_request()

    @register("pt-BR", ".*desligar.*sala.*")
    def st_room_off(self, speech, language):
        resposta = self.ask(u"Direta ou Indireta?")
        if resposta == "Direta":
        	self.say("{0}","")
            self.say("Desligando as luzes da sala.","Turning off living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_1.jar'")
        else if resposta == "Indireta":
        	self.say("{0}","")
            self.say("Desligando as luzes da sala.","Turning off living room lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_2.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_3.jar'")
        else:
        	self.say("{0}","")
        	self.say("Desculpe, nao entendi.","Sorry, I didn't get that.")	
	self.complete_request()