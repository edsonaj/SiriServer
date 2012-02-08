#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class garagemcontrol(Plugin):
    
    @register("pt-BR", "(.*ligar.*garagem.*)")
    def st_garage_on(self, speech, language):
        self.say("Ligando as luzes da garagem.","Turning on garage lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Garage__Turn_Light_ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*garagem.*)")
    def st_garage_off(self, speech, language):
        self.say("Desligando as luzes da garagem.","Turning off garage lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Garage__Turn_Light_OFF.jar'")
        self.complete_request()
