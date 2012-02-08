#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from plugin import *

class cinemacontrol(Plugin):

    @register("pt-BR", "(.*ligar.*cinema.*)")
    def st_cinemaon(self, speech, language):
        self.say("Ligando as luzes do cinema.","Turning on cinema lights") 
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Turn_Light_ON.jar'")
        self.complete_request()

    @register("pt-BR", "(.*desligar.*cinema.*)")
    def st_cinemaoff(self, speech, language):
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
    
    @register("pt-BR", "(.*assistir.*filme.*)")
    def st_assistir_filme(self, speech, language):
        self.say("Preparando a sala de cinema para voce.","Setting the room for you")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Turn_Light_OFF.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Dimmer_40.jar'")
        os.system("java -jar '/home/ubuntu/SiriProxy/KNX/_Cinema__Close_Windows.jar'")
        self.say("A sala esta pronta. Tenha um bom filme.","The room is ready. Have a great film.")
        self.complete_request()

 