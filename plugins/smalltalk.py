#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugin import *

class smalltalk(Plugin):
    
    @register("pt-BR", "(.*Ola.*)|(.*Oi.*Siri.*)")
    @register("en-US", "(.*Ola.*)|(.*Oi.*Siri.*)")
    def st_hello(self, speech, language):
        if language == 'pt-BR':
            self.say("Ola.")
        else:
            self.say("Hello")
        self.complete_request()

    @register("pt-BR", "(.*Oi.*)|(.*Ola.*Siri.*)")
    @register("en-US", "(.*Oi.*)|(.*Ola.*Siri.*)")
    def st_hello(self, speech, language):
        if language == "pt-BR":
            self.say("Ol‡.")
        else:
            self.say("Hello")
        self.complete_request()
    
    @register("pt-BR", ".*seu nome.*")
    @register("en-US", ".*seu nome.*")
    def st_name(self, speech, language):
        if language == "pt-BR":
            self.say("Meu nome Ž Siri.")
        else:
            self.say("Siri.")
        self.complete_request()
    
    @register("pt-BR", "Como voce esta?")
    @register("en-US", "How are you?")
    def st_howareyou(self, speech, language):
        if language == 'pt-BR':
            self.say("Muito bem, obrigada por perguntar.")
        else:
            self.say("Fine, thanks for asking!")
        self.complete_request()
    
    @register("pt-BR", ".*Obrigado.*")
    @register("en-US", ".*Thank.*you.*")
    def st_thank_you(self, speech, language):
        if language == 'pt-BR':
            self.say("ƒ s— o meu trabalho.")
        else:
            self.say("You are welcome.")
            self.say("This is my job.")
        self.complete_request()     
    
    @register("pt-BR", "(.*quer.*casar.*)|(.*vamos.*casar.*)")
    @register("en-US", ".*Want.*marry*")
    def st_marry_me(self, speech, language):
        if language == 'pt-BR':
            self.say("Desculpe, mas estou apaixonada pelo iPhone Preto de seu amigo. Mas n—s ainda podemos ser amigos.")            
        else:
            self.say("No thank you, I'm in love with the black iPhone from you friend.")
        self.complete_request()
    
    @register("de-DE", ".*erzähl.*Witz.*")
    @register("en-US", ".*tell.*joke*")
    def st_tell_joke(self, speech, language):
        if language == 'de-DE':
            self.say("Zwei iPhones stehen an der Bar ... den Rest habe ich vergessen.")            
        else:
            self.say("Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()
    
    @register("de-DE", ".*erzähl.*Geschichte.*")
    @register("en-US", ".*tell.*story*")
    def st_tell_story(self, speech, language):
        if language == 'de-DE':
            self.say("Es war einmal ... nein, es ist zu albern")            
        else:
            self.say("Far far away, there was ... no, too stupid")
        self.complete_request()
    
    @register("de-DE", "(.*Was trägst Du?.*)|(.*Was.*hast.*an.*)")
    @register("en-US", ".*what.*wearing*")
    def st_tell_clothes(self, speech, language):
        if language == 'de-DE':
            self.say("Das kleine schwarze oder war es das weiße?")
            self.say("Bin morgends immer so neben der Spur.")  
        else:
            self.say("I guess the small black one, or was it white?")
        self.complete_request()
    
    @register("de-DE", ".*Bin ich dick.*")
    @register("en-US", ".*Am I fat*")
    def st_fat(self, speech, language):
        if language == 'de-DE':
            self.say("Dazu möchte ich nichts sagen.")            
        else:
            self.say("I would prefer not to say.")
        self.complete_request()
