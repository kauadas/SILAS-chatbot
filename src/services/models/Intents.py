import pickle



class Intent:
    def __init__(self, name, phrases, required_entities, optional_entities, function):
        self.name = name

        self.phrases = phrases
        self.lemmas = None
        self.tags = None
        self.deps = None


        self.required_entities = required_entities
        self.optional_entities = optional_entities

        self.function = function

    def process(self, doc):

        final_phrases = []
        tags = []
        deps = []
        for training_phrase in self.phrases:
            doc_ = doc(training_phrase.lower())
            final_phrases.append(doc_.lemmas)
            tags.append(doc_.pos)
            deps.append(doc_.deps)

        self.lemmas = final_phrases
        self.tags = tags
        self.deps = deps


    def context(self, ctx):
        return 0


class IntentsGroup:
    def __init__(self, intents):
        self.intents = intents
        self.is_processed = False
        self.weights = {}

    def process(self, nlp):
        for intent in self.intents:
            intent.process(nlp)

        self.is_processed = True
        print("Intents processed")

        self.gen_weights()

    def gen_weights(self):
        for intent in self.intents:
            unique_lemmas = set()
            for phrase in intent.lemmas:
                unique_lemmas.update(phrase)

            for lema in unique_lemmas:
                self.weights[lema] = self.weights.get(lema, 0) + 1

        for lema in self.weights:
            self.weights[lema] = 1 / self.weights[lema]

    def get_weight(self, lema):
        return self.weights.get(lema, 0)

    def get_intent(self, intent_name):
        for intent in self.intents:
            if intent.name == intent_name:
                return intent

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename) -> "IntentsGroup":
        with open(filename, "rb") as f:
            return pickle.load(f)
