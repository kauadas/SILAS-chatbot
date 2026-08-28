from .models.Intents import IntentsGroup
from .IntentDetector import IntentDetector
from .Context import Context
from .models.Entitys import EntitysGroup


class NaturalProcessing:
    def __init__(self, intents: IntentsGroup, entitys: EntitysGroup):
        
        self.intents = intents
        self.entitys = entitys

        if not self.intents.is_processed:
            raise Exception("Intents are not processed")

        self.intentsDetector = IntentDetector(self.intents)

        self.context = Context()
        self.context.state = "start"

    def process(self, message):
        Value = self.intentsDetector.detect_intent(message)
        return Value
