#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class cozinhacontrol(Plugin):
    
    @register("pt-BR", ".*ligar cozinha.*")
    def st_kitchenon(self, speech, language):
        self.say("Ligando as luzes da cozinha.","Turning on kitchen lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_2.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar cozinha.*)")
    def st_kitchenoff(self, speech, language):
        self.say("Desligando as luzes da cozinha.","Turning off kitchen lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_2.jar'")
        self.complete_request()
