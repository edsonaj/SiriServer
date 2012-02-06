# -*- coding: utf-8 -*-
#Siri Server plugin - Portugues

from plugin import *

class portugues(Plugin):
    

    @register("pt-BR", "(.*Olá.*)|(.*Olá.*Siri.*)|(.*Oi.*)|(.*Oi.*Siri.*)")
    def st_hello(self, speech, language):
        self.say("Olá","Hello")
        self.complete_request()

    @register("pt-BR", "(.*seu nome.*)")
    def st_name(self, speech, language):
        self.say("Meu nome é Siri.","My name is Siri.")
        self.complete_request()
    
    @register("pt-BR", "(.*Como.*você.*está.*)")
    def st_howareyou(self, speech, language):
        self.say("Muito bem, obrigada por perguntar!","Fine, thanks for asking!")
        self.complete_request()
    
    @register("pt-BR", ".*Obrigado.*")
    def st_thank_you(self, speech, language):
        self.say("De nada.","You are welcome.")
        self.say("É apenas meu trabalho.","This is my job.")
        self.complete_request()     
    
    @register("pt-BR", "(.*quer.*casar.*)|(.*vamos.*casar.*)")
    def st_marry_me(self, speech, language):
        self.say("Não, obrigada. Eu estou apaixonada pelo iPhone preto do seu amigo.","No, thank you. I'm in love with the black iPhone from your friend.")
        self.complete_request()
    
    @register("pt-BR", "(.*conte.*piada*)|(.*contar.*piada.*)")
    def st_tell_joke(self, speech, language):
        self.say("Dois iPhones entraram em um bar ... Esqueci o resto.","Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()

    @register("pt-BR", "(.*conte.*historia*)|(.*contar.*historia.*)")
    def st_tell_story(self, speech, language):
        self.say("Muito, mas muito distante, existia ... não, muito estupida esta história.","Far far away, there was ... no, too stupid")
        self.complete_request()
    
    @register("pt-BR", ".*significado.*vida.*")
    def st_tell_story(self, speech, language):
        self.say("Eu não sei, mas deve ter algum app para isso.","I don't know, but it should have an app for that")
        self.complete_request()