#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class jantarcontrol(Plugin):
    
    @register("pt-BR", ".*ligar.*jantar.*")
    def st_kitchenon(self, speech, language):
        self.say("Ligando as luzes da sala de jantar.","Turning on dinner room lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_DinnerRoom__Turn_Light_ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*jantar.*)")
    def st_kitchenoff(self, speech, language):
        self.say("Desligando as luzes da sala de jantar.","Turning off dinner room lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_DinnerRoom__Turn_Light_OFF.jar'")
        self.complete_request()
