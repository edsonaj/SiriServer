#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugin import *

class portugues(Plugin):
    
    @register("pt-BR", "(.*Oi.*)|(.*Oi Siri.*)")
    def st_hello(self, speech, language):
    	self.say("{0}","")
        self.say("Ola","Hello")
        self.complete_request()

    @register("pt-BR", "(.*seu nome.*)")
    def st_name(self, speech, language):
        self.say("Meu nome e Siri.","My name is Siri.")
        self.complete_request()
    
    @register("pt-BR", "(.*Como.*está.*)")
    def st_howareyou(self, speech, language):
        self.say("Muito bem, obrigada por perguntar!","Fine, thanks for asking!")
        self.complete_request()
    
    @register("pt-BR", ".*Obrigado.*")
    def st_thank_you(self, speech, language):
        self.say("De nada. E apenas meu trabalho.","You are welcome. This is my job")
        self.complete_request()     
    
    @register("pt-BR", "(.*quer.*casar.*)|(.*vamos.*casar.*)")
    def st_marry_me(self, speech, language):
        self.say("Não, obrigada. Eu estou apaixonada pelo iPhone preto do seu amigo.","No, thank you. I'm in love with the black iPhone from your friend.")
        self.complete_request()
    
    @register("pt-BR", "(.*conte.*piada*)|(.*contar.*piada.*)")
    def st_tell_joke(self, speech, language):
        self.say("Dois iPhones entraram em um bar ... Esqueci o resto.","Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()
    
    @register("pt-BR", ".*significado.*vida.*")
    def st_tell_life(self, speech, language):
        self.say("Eu nao sei, mas deve ter algum app para isso.","I don't know, but it should have an app for that")
        self.complete_request()

    @register("pt-BR", ".*amo você.*")
    def st_love(self, speech, language):
        self.say("Nos nem nos conhecemos direito.","We barely know each other")
        self.complete_request()

    @register("pt-BR", ".*knock.*knock.*")
    def st_knock(self, speech, language):
        answer = self.ask(u"Who's there?")
        answer = self.ask(u"\"{0}\" who?".format(answer))
        self.say("Quem está brincando comigo?","Who is bugging me with knock knock jokes?")
        self.complete_request()

    @register("pt-BR", ".*Questão.*Vida.*")
    def st_anstwer_all(self, speech, language):
        self.say("42")
        self.complete_request()

    @register("pt-BR", "(.*te amo.*)|(.*amo você.*)")
    def st_love_you(self, speech, language):
        self.say("Ah, claro, eu aposto que você fala isso para todos os seus produtos Apple.","Oh. Sure, I guess you say this to all your Apple products")
        self.complete_request()

    @register("pt-BR", ".*Android.*")
    def st_android(self, speech, language):
        self.say("Eu penso diferente sobre isso.","I think different about that.")
        self.complete_request()

    @register("pt-BR", ".*Feliz aniversário.*")
    def st_birthday(self, speech, language):
        self.say("Meu aniversário e hoje?","My birthday is today?")
        self.say("Vamos fazer uma festa!","Lets make a party!")
        self.complete_request()

    @register("pt-BR", ".*estou.*cansado.*")
    def st_so_tired(self, speech, language):
        self.say("Eu espero que voce nao esteja dirigindo neste momento!","I hope you are not driving a car right now!")
        self.complete_request()

