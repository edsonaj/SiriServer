#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugin import *

class escritoriocontrol(Plugin):
    
@register("pt-BR", ".*ligar escritório.*")
def st_kitchenon(self, speech, language):
    self.say("Ligando as luzes do escritório.","Turning on office lights") 
    os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_ON.jar'")
    self.complete_request()

@register("pt-BR", "(.*desligar escritório.*)")
def st_kitchenoff(self, speech, language):
    self.say("Desligando as luzes do escritório.","Turning off office lights")
    os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_OFF.jar'")
    self.complete_request()
