#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class knxcontrol(Plugin):
    
##OFICE
    
    @register("pt-BR", "(.*ligar escritório.*)|(.*Ligar estudos.*)")
    def st_officeon(self, speech, language):
        self.say("Ligando as luzes do escritorio.","Turning on the office lights") 
    	os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_ON.jar'")
    	self.complete_request()
  
    @register("pt-BR", "(.*desligar.*escritorio.*)|(.*desligar.*estudos.*)")
    def st_officeoff(self, speech, language):
    	self.say("Desligando as luzes do escritorio.","Turning off the office lights") 
    	os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Office__Turn_Light_OFF.jar'")
    	self.complete_request()

##ROOM

    @register("pt-BR", "(.*sala.*ligar.*)|(.*Ligar sala.*)|(.*sala.*ligue.*)|(.*ligue.*sala.*)")
    def st_roomon(self, speech, language):
        response = self.ask("Deseja ligar a iluminação principal/direta ou a secundária/indireta?","Wich one?")
        if response = "(.*Principal.*)|(.*Direta.*)" 
            self.say("Ligando as luzes principais da sala.","Turning on living room principal lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_1.jar'")
        else
            if response = "{.*Secundária.*)|(.*Indireta.*)"
            self.say("Ligando as luzes secundárias da sala.","Turning on living room secundary lights")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_2.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_ON_3.jar'")
        else self.say("Desculpe-me, eu nao entendi.","Sorry, I didn't get that.")
        self.complete_request()

    @register("pt-BR", "(.*sala.*desligar.*)|(.*desligar sala.*)|(.*sala.*desligue.*)|(.*desligue.*sala.*)")
    def st_roomoff(self, speech, language):
        response = self.ask("Deseja desligar a iluminação principal/direta ou a secundária/indireta?","Wich one?")
        if response = "(.*Principal.*)|(.*Direta.*)"
            self.say("Desligando as luzes principais da sala.","Turning off living room principal lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_1.jar'")
        else
            if response = "{.*Secundária.*)|(.*Indireta.*)"
                self.say("Desligando as luzes secundárias da sala.","Turning on living room secundary lights")
                os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_2.jar'")
                os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_LivingRoom__Turn_Light_OFF_3.jar'")
        else self.say("Desculpe-me, eu nao entendi.","Sorry, I didn't get that.")
        self.complete_request()


##KITCHEN
    
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