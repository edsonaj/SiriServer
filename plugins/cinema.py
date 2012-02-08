#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class cinemacontrol(Plugin):

    @register("pt-BR", "(.*ligar.*cinema.*)")
    def st_cinema_on(self, speech, language):
        self.say("Ligando as luzes do cinema.","Turning on cinema lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Turn_Light_ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*cinema.*)")
    def st_cinema_off(self, speech, language):
        self.say("Desligando as luzes do cinema.","Turning off cinema lights")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Turn_Light_OFF.jar'")
        self.complete_request()
        
    @register("pt-BR", "(.*abrir.*persiana.*)")
    def st_cinema_open(self, speech, language):
        self.say("Abrindo a persiana do cinema.","Opening the cinema blinds") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Open_Window.jar'")
        self.complete_request()

    @register("pt-BR", "(.*fechar.*persiana.*)")
    def st_cinema_close(self, speech, language):
        self.say("Fechando a persiana do cinema.","Closing the cinema blinds")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Close_Windows.jar'")
        self.complete_request()
    
    @register("pt-BR", "(.*assistir.*filme.*)|(.*prepare.*cinema.*)")
    def st_assistir(self, speech, language):
        self.say("Preparando a sala de cinema para voce.","Setting the room for you")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Turn_Light_OFF.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Dimmer_40.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Close_Windows.jar'")
        self.say("A sala esta pronta. Tenha um bom filme.","The room is ready. Have a great film.")
        self.complete_request()

    @register("pt-BR", ".*filme.*acabou.*")
    def st_acabou(self, speech, language):
        resposta = self.ask(u"Deseja abrir a persiana também?")
        if resposta == "Sim":
            self.say("Ligando a iluminacao de chao e abrindo as persianas.","turning on the ground lights and opening the blind") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Open_Window.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Turn_Light_OFF.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Dimmer_100.jar'")
        else if resposta == "Não":
            self.say("Ligando a iluminacao de chao.","turning on the ground lights") 
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Turn_Light_OFF.jar'")
            os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Dimmer_100.jar'")
        else: 
        	self.say("Desculpe, nao entendi.","Sorry, I didn't get that.")
        self.say("Espero que tenha sido um bom filme.","I hope it was a great movie.")
		self.complete_request()