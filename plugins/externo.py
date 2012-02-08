#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class externocontrol(Plugin):
    
    @register("pt-BR", "(.*ligar.*piscina.*)")
    def st_poolon(self, speech, language):
        self.say("Ligando a bomba da piscina.","Turning on the pool") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Pool__ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*piscina.*)")
    def st_pooloff(self, speech, language):
        self.say("Desligando a bomba da piscina.","Turning off the pool")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Pool__OFF.jar'")
        self.complete_request()
        
    @register("pt-BR", "(.*ligar.*parede.*)|(.*ligar.*fundos.*)")
    def st_wallon(self, speech, language):
        self.say("Ligando as luzes da parede do fundo.","Turning on the back wall lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Pool__Turn_Light_ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*parede.*)|(.*desligar.*fundos.*)")
    def st_walloff(self, speech, language):
        self.say("Desligando as luzes da parede do fundo.","Turning off back wall lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Pool__Turn_Light_OFF.jar'")
        self.complete_request()
        
    @register("pt-BR", "(.*ligar.*bar.*)|(.*liga.*bar.*)|(.*ligue.*bar.*)")
    def st_bar_on(self, speech, language):
        self.say("Ligando as luzes do bar.","Turning on bar lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Bar__Turn_Light_ON_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Bar__Turn_Light_ON_2.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*bar.*)")
    def st_bar_off(self, speech, language):
        self.say("Desligando as luzes do bar.","Turning off bar lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Bar__Turn_Light_OFF_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Bar__Turn_Light_OFF_2.jar'")
        self.complete_request()
        
    @register("pt-BR", "(.*ligar.*led.*)")
    def st_barled_on(self, speech, language):
        self.say("Ligando os LEDs do bar.","Turning on bar led lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Bar__Turn_Light_ON_3.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*led.*)")
    def st_barled_off(self, speech, language):
        self.say("Desligando os LEDs do bar.","Turning off bar led lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Bar__Turn_Light_OFF_3.jar'")
        self.complete_request()
        
        
    @register("pt-BR", "(.*ligar.*varanda.*)")
    def st_outside_on(self, speech, language):
        self.say("Ligando as luzes da varanda.","Turning on outside lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Outside__Turn_Lights_ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*varanda.*)")
    def st_outside_off(self, speech, language):
        self.say("Desligando as luzes da varanda.","Turning off outside lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Outside__Turn_Lights_OFF.jar'")
	self.complete_request()