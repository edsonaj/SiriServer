#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib2, urllib
import json
import logging
from uuid import uuid4
from plugin import *

from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.systemObjects import DomainObject

class NoteSnippet(AceObject):
    def __init__(self, notes=None):
        super(NoteSnippet, self).__init__("Snippet", "com.apple.ace.note")
        self.notes = notes if notes != None else []
    
    def to_plist(self):
        self.add_property('notes')
        return super(NoteSnippet, self).to_plist()


class NoteObject(AceObject):
    def __init__(self, contents="", identifier=""):
        super(NoteObject, self).__init__("Object", "com.apple.ace.note")
        self.contents = contents
        self.identifier = identifier
    def to_plist(self):
        self.add_property('contents')
        self.add_property('identifier')
        return super(NoteObject, self).to_plist()

class Create(ClientBoundCommand):
    def __init__(self, refId=None, aceId=None, contents=""):
        super(Create, self).__init__("Create", "com.apple.ace.note", None, None)
        self.contents = contents
        self.aceId= aceId if aceId != None else str.upper(str(uuid4()))
        self.refId = refId if refId != None else str.upper(str(uuid4()))
        
    def to_plist(self):
    	self.add_item('aceId')
        self.add_item('refId')
        self.add_property('contents')
        return super(Create, self).to_plist()

class note(Plugin):
    localizations = {"noteDefaults": 
                        {"searching":{"pt-BR": "Criando sua nota ..."}, 
                         "result": {"pt-BR": "Aqui esta sua nota:"},
                         "nothing": {"pt-BR": "O que eu devo anotar?"}}, 
                    "failure": {
                                "pt-BR": "Eu nao posso anotar agora."
                                }
                    }
    @register("pt-BR", "(.*anote [a-zA-Z0-9]+)")
    def writeNote(self, speech, language):
        content_raw = re.match(".*anote ([a-zA-Z0-9, ]+)$", speech, re.IGNORECASE)
        if content_raw == None:
            view_initial = AddViews(self.refId, dialogPhase="Reflection")
            view_initial.views = [AssistantUtteranceView(text=note.localizations['noteDefaults']['nothing']["pt-BR"], speakableText=note.localizations['noteDefaults']['nothing']["pt-BR"], dialogIdentifier="Note#failed")]
            self.sendRequestWithoutAnswer(view_initial)
        else:
            view_initial = AddViews(self.refId, dialogPhase="Reflection")
            view_initial.views = [AssistantUtteranceView(text=note.localizations['noteDefaults']['searching']["pt-BR"], speakableText=note.localizations['noteDefaults']['searching']["pt-BR"], dialogIdentifier="Note#creating")]
            self.sendRequestWithoutAnswer(view_initial)
            
            content_raw = content_raw.group(1).strip()
            if "que" in content_raw:
                split = content_raw.split(' ')
                if split[0] == "que":
                    split.pop(0)
                    content_raw = ' '.join(map(str, split))
                
            note_create = Create()
            note_create.contents = content_raw
            note_return = self.getResponseForRequest(note_create)
        
            view = AddViews(self.refId, dialogPhase="Summary")
            view1 = AssistantUtteranceView(text=note.localizations['noteDefaults']['result']["pt-BR"], speakableText=note.localizations['noteDefaults']['result']["pt-BR"], dialogIdentifier="Note#created")
        
            note_ = NoteObject()
            note_.contents = content_raw
            note_.identifier = note_return["properties"]["identifier"]
        
            view2 = NoteSnippet(notes=[note_])
            view.views = [view1, view2]
            self.sendRequestWithoutAnswer(view)
        self.complete_request()

    