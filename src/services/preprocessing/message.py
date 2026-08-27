import spacy

class Message:
    def __init__(self, nlp, message):
        self.content = message
        self.nlp = nlp
        self.normalize()
        self.tokenize()
        self.lemmatize()
        self.classify()

    def normalize(self):
        self.normalized = self.content.lower()
        self.normalized = self.normalized.strip()

        return self.normalized

    def tokenize(self):
        doc = self.nlp(self.normalized)
        self.tokens = [token for token in doc]
        return self.tokens

    def lemmatize(self):
        self.lemmas = [token.lemma_ for token in self.tokens]
        return self.lemmas

    def classify(self):
        self.tags = [token.pos_ for token in self.tokens]
        return self.tags



if __name__ == "__main__":
    nlp = spacy.load("pt_core_news_sm")
    message = Message(nlp, "Os gatos estavam correndo no telhado!")
    print(message.normalized)
    print(message.tokens)
    print(message.lemmas)

    for item in message.tokens:
        print(item.lemma_, item.pos_, item.dep_)