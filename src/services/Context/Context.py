

class Context:
    def __init__(self):
        self.last_intent = None
        self.last_entities = {}
        self.last_message = None
        self.state = None
        self.humor = 0

        self.history = []


    def remember(self, intent, entities, message):
        self.last_intent = intent
        self.last_entities = entities
        self.last_message = message
        self.history.append((intent, entities, message))