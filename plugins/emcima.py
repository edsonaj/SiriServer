#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class upstairscontrol(Plugin):
    
    @register("pt-BR", "(.*ligar.*corredor.*)|(.*liga.*corredor.*)|(.*ligue.*corredor.*)")
    def st_hall_on(self, speech, language):
        self.say("Ligando as luzes do corredor no piso superior.","Turning on upstairs lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Upstairs__Turn_Light_ON_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Upstairs__Turn_Light_ON_2.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*corredor.*)|(.*desliga.*corredor.*)|(.*desligue.*corredor.*)")
    def st_hall_off(self, speech, language):
        self.say("Desligando as luzes do corredor no piso superior.","Turning off upstairs lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Upstairs__Turn_Light_OFF_1.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Upstairs__Turn_Light_OFF_2.jar'")
        self.complete_request()

	@register("pt-BR", "(.*ligar.*escada.*)|(.*liga.*escada.*)|(.*ligue.*escada.*)|(.*ligar.*pé direito.*)|(.*liga.*pé direito.*)|(.*ligue.*pé direito.*)")
    def st_stairs_on(self, speech, language):
        self.say("Ligando as luzes do pé direito duplo.","Turning on stairs lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Stairs__Turn_Light_OFF.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*escada.*)|(.*desliga.*escada.*)|(.*desligue.*escada.*)|(.*desligar.*pé direito.*)|(.*desliga.*pé direito.*)|(.*desligue.*pé direito.*)")
    def st_stairs_off(self, speech, language):
        self.say("Desligando as luzes do pé direito duplo.","Turning off stairs lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Stairs__Turn_Light_ON.jar'")
        self.complete_request()