import pickle

class Intent:
    def __init__(self, name, phrases, required_entities, optional_entities, function, response_corpus):
        self.name = name
        self.phrases = phrases
        self.lemmas = None
        self.structure = None
        self.required_entities = required_entities
        self.optional_entities = optional_entities
        self.function = function
        self.response_corpus = response_corpus

    def process(self, nlp):

        final_phrases = []
        structure = []
        for training_phrase in self.phrases:
            doc = nlp(training_phrase.lower())
            final_phrases.append([token.lemma_ for token in doc])
            structure.append([token.pos_ for token in doc])

        self.lemmas = final_phrases
        self.structure = structure


class IntentsGroup:
    def __init__(self, intents):
        self.intents = intents
        self.is_processed = False

    def process(self, nlp):
        for intent in self.intents:
            intent.process(nlp)

        self.is_processed = True
        print("Intents processed")

    def get_intent(self, intent_name):
        for intent in self.intents:
            if intent.name == intent_name:
                return intent

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
