#Siri Server plugin - Portugues

from plugin import *

class portugues(Plugin):
    

    @register("en-US", "(.*Ola.*)|(.*Ola.*Siri.*)|(.*Oi.*)|(.*Oi.*Siri.*)")
    def st_hello(self, speech, language):
        self.say("Ola","Hello")
        self.complete_request()

    @register("en-US", ".*seu nome.*")
    def st_name(self, speech, language):
        self.say("Meu nome e Siri.","My name is Siri.")
        self.spoken("My name is Edson")
        self.complete_request()
    
    @register("en-US", ".*Como.*voce.*esta.*")
    def st_howareyou(self, speech, language):
        self.say("Muito bem, obrigada por perguntar!","Fine, thanks for asking!")
        self.complete_request()
    
    @register("en-US", ".*Obrigado.*")
    def st_thank_you(self, speech, language):
        self.say("De nada.","You are welcome.")
        self.say("E apenas meu trabalho.","This is my job.")
        self.complete_request()     
    
    @register("en-US", "(.*quer.*casar.*)|(.*vamos.*casar.*)")
    def st_marry_me(self, speech, language):
        self.say("NAo, obrigada. Eu estou apaixonada pelo iPhone preto do seu amigo.","No, thank you. I'm in love with the black iPhone from your friend.")
        self.complete_request()
    
    @register("en-US", "(.*conte.*piada*)|(.*contar.*piada*)")
    def st_tell_joke(self, speech, language):
        self.say("Dois iPhones entraram em um bar ... Esqueci o resto.","Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()
    
    @register("en-US", "(.*conte.*historia*)|(.*contar.*historia*)")
    def st_tell_story(self, speech, language):
        self.say("Muito, mas muito distante, existia ... nao, muito estupida.","Far far away, there was ... no, too stupid")
        self.complete_request()
    
    @register("en-US", ".*significado.*vida*")
    def st_tell_story(self, speech, language):
        self.say("Eu nao seu, mas deve haver um app para isso.","I don't know, but it should have an app for that")
        self.complete_request()