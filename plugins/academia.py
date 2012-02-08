#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class academiacontrol(Plugin):
    
    @register("pt-BR", ".*ligar academia.*")
    def st_gymon(self, speech, language):
        self.say("Ligando as luzes da academia.","Turning on gym lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_GYM__ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar academia.*)")
    def st_gymoff(self, speech, language):
        self.say("Desligando as luzes da academia.","Turning off gym lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_GYM__OFF.jar'")
        self.complete_request()
