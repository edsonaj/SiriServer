#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class knxcontrol(Plugin):

    @register("pt-BR", "(.*cozinha.*ligar.*)|(.*ligar cozinha.*)|(.*cozinha.*ligue.*)|(.*ligue.*cozinha.*)")
    def st_kitchenon(self, speech, language):
        self.say("Ligando as luzes da cozinha.","Turning on kitchen lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_2.jar'")
        self.complete_request()
    
    @register("pt-BR", "(.*cozinha.*desligar.*)|(.*desligar cozinha.*)|(.*cozinha.*desligue.*)|(.*desligue.*cozinha.*)")
    def st_kitchenoff(self, speech, language):
        self.say("Desligando as luzes da cozinha.","Turning off kitchen lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_2.jar'")
        self.complete_request()