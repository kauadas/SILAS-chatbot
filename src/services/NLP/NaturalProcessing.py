from ..models.Intents import IntentsGroup
from .IntentDetector import IntentDetector
from ..Context.Context import Context
from ..models.Entitys import EntitysGroup
from ..CFG.Grammar import Grammar


class NLPResponse:
    def __init__(self, intent, entities):
        self.intent = intent
        self.entities = entities

class NaturalProcessing:
    def __init__(self, intents: IntentsGroup, entitys: EntitysGroup, grammar: Grammar):
        
        self.intents = intents
        self.entitys = entitys
        self.grammar = grammar

        if not self.intents.is_processed:
            raise Exception("Intents are not processed")

        self.intentsDetector = IntentDetector(self.intents, self.grammar)

        self.context = Context()
        self.context.state = "start"

    def process(self, message):
        Value = self.intentsDetector.detect_intent(message)
        return Value
