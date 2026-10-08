
class GeneratorContext:
    def __init__(self, intent, variables):
        self.intent = intent
        self.variables = variables
        

class TrainingContext:
    def __init__(self):
        self.context_chain = []