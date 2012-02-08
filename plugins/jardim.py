#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class jardimcontrol(Plugin):
    
    @register("pt-BR", ".*ligar.*jardim.*")
    def st_gardenon(self, speech, language):
        self.say("Ligando o jardim interno.","Turning on the internal garden") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Garden_ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*jardim.*)")
    def st_gardenoff(self, speech, language):
        self.say("Desligando o jardim internoa.","Turning off the internal garden")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Garden_OFF.jar'")
        self.complete_request()
