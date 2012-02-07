#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class automacao(Plugin):

@register("pt-BR", "(.*cozinha ligar.*)|(.*ligar cozinha.*)|(.*cozinha.*ligue.*)|(.*ligue a cozinha.*)")
def st_kitchenon(self, speech, language):
    self.say("Ligando as luzes da cozinha.","Turning on kitchen lights") 
    os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_1.jar'")
    os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_ON_2.jar'")
    self.complete_request()
    
@register("pt-BR", "(.*cozinha desligar.*)|(.*desligar cozinha.*)|(.*desligue a cozinha.*)")
def st_kitchenoff(self, speech, language):
    self.say("Desligando as luzes da cozinha.","Turning off kitchen lights")
    os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_1.jar'")
    os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Kitchen__Turn_Light_OFF_2.jar'")
    self.complete_request()





@register("pt-BR", "(.*escritório ligar.*)|(.*ligar escritório.*)|(.*ligue o escritório.*)")
def st_officeon(self, speech, language):
    self.say("Ligando as luzes do escritório.","Turning on office lights") 
    os.system("java -jar '/home/siriproxy/KNX/_Office__Turn_Light_ON.jar'")
    self.complete_request()

@register("pt-BR", "(.*escritório desligar.*)|(.*desligar escritório.*)|(.*desligue o escritório.*)")
def st_officeoff(self, speech, language):
    self.say("Desligando as luzes do escritório.","Turning off office lights")
    os.system("java -jar '/home/siriproxy/KNX/_Office__Turn_Light_OFF.jar'")
    self.complete_request()