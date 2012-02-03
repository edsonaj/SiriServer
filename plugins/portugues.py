#Siri Server plugin - Portugues

from plugin import *

class portugues(Plugin):
    

    @register("en-US", "(.*Ola.*)|(.*Ola.*Siri.*)|(.*Oi.*)|(.*Oi.*Siri.*)")
    def st_hello(self, speech, language):
        self.say("Hello")
        self.complete_request()


    @register("en-US", ".*seu nome.*")
    def st_name(self, speech, language):
        self.say("My name is Siri.")
        self.complete_request()
    
    @register("en-US", "Como voce esta?")
    def st_howareyou(self, speech, language):
        self.say("Fine, thanks for asking!")
        self.complete_request()
    
    @register("en-US", ".*Obrigado.*")
    def st_thank_you(self, speech, language):
        self.say("You are welcome.")
        self.say("This is my job.")
        self.complete_request()     
    
    @register("en-US", "(.*quer.*casar.*)|(.*vamos.*casar.*)")
    def st_marry_me(self, speech, language):
        self.say("No thank you, I'm in love with the black iPhone from you friend.")
        self.complete_request()
    
    @register("en-US", "(.*conte.*piada*)|(.*contar.*piada*)")
    def st_tell_joke(self, speech, language):
        self.say("Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()
    
    @register("en-US", "(.*conte.*historia*)|(.*contar.*historia*)")
    def st_tell_story(self, speech, language):
        self.say("Far far away, there was ... no, too stupid")
        self.complete_request()
    
    @register("en-US", ".*significado.*vida*")
    def st_tell_story(self, speech, language):
        self.say("I don't know, but it should have an app for that")
        self.complete_request()