
def NLUTEST():
    from services.NLP.natural_processing import NaturalProcessing
    from services.NLP.models.Intents import IntentsGroup, Intent
    from services.Vocabulary import Vocabulary
    import spacy
    import json
    nlp = spacy.load("pt_core_news_sm")


    # intents = []


    # with open("test.json", "r") as f:
    #     data = json.load(f)

    # for intent in data["intents"]:
    #     intents.append(Intent(intent["name"], intent["phrases"], [], [], None, None))

    # intents = IntentsGroup(intents)
    # intents.process(nlp)

    # intents.save("intents.pkl")

    intents = IntentsGroup.load("intents.pkl")
    intents.vocab = []
    intents.gen_vocab()

    vocab = Vocabulary(intents.vocab)

    print(len(intents.intents))


    from services.preprocessing.message import Message
    natural_processing = NaturalProcessing(intents, None)
    test = input(" >> ")
    #test = vocab.normalize_phrase(test)
    #print(test)
    message = Message(nlp, test)
  

    print([intents.get_weight(token.lemma_) for token in message.tokens])
    intent = natural_processing.process(message)


    print("para a mensagem: ", test, "foi detectado o seguinte intent:")
    print("intent", "lex", "stc", "ent", "ctx", "total")
    for i in intent:
        print(i.intent.name, i.lexical_score, i.structural_score, i.entity_score, i.context_score, i.total_score())


if __name__ == "__main__":
    NLUTEST()