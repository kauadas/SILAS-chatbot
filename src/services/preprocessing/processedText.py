

class ProcessedText:
    def __init__(self, content, doc):
        self.content = content
        self.doc = doc(content)

        self.tokens = self.doc["tokens"]
        self.lemmas = self.doc["lemmas"]
        self.tags = self.doc["pos"]
        self.deps = self.doc["deps"]

        self.normalized = self.normalize()


    def normalize(self):
        self.normalized = self.content.lower()
        self.normalized = self.normalized.strip()

        return self.normalized

if __name__ == "__main__":
    import spacy
    nlp = spacy.load("pt_core_news_sm")
    doc_ = nlp("Os gatos estavam correndo no telhado!")
    doc = {"tokens": [], "lemmas": [], "pos": [], "deps": []}
    for token in doc_:
        doc["tokens"].append(token)
        doc["lemmas"].append(token.lemma_)
        doc["pos"].append(token.pos_)
        doc["deps"].append(token.dep_)

    ProcessedText = ProcessedText("Os gatos estavam correndo no telhado!", **doc)

    print(ProcessedText.normalized)
    print(ProcessedText.tokens)
    print(ProcessedText.lemmas)

    for item in ProcessedText.tokens:
        print(item.lemma_, item.pos_, item.dep_)