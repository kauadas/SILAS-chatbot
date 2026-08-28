

class Context:
    def __init__(self):
        self.last_intent = None
        self.last_entities = {}
        self.last_message = None
        self.state = None

        self.history = []