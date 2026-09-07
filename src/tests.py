

def regenerate_intents():
    from services.NLP.models.Intents import IntentsGroup, Intent

    import spacy
    import json
    nlp = spacy.load("pt_core_news_sm")
    intents = []
    
    
    with open("test.json", "r") as f:
        data = json.load(f)

    for intent in data["intents"]:
        intents.append(Intent(intent["name"], intent["phrases"], [], [], None, None))

    intents = IntentsGroup(intents)
    intents.process(nlp)

    intents.save("intents.pkl")
    print("Intents regenerated and saved to intents.pkl")

def NLPTEST():
    from services.NLP.NaturalProcessing import NaturalProcessing
    from services.NLP.models.Intents import IntentsGroup, Intent
    import spacy
    nlp = spacy.load("pt_core_news_sm")


   

    intents = IntentsGroup.load("intents.pkl")
    intents.vocab = []
    intents.gen_vocab()

    print(len(intents.intents))


    from services.preprocessing.message import Message
    natural_processing = NaturalProcessing(intents, None)
    test = input(" >> ")
    message = Message(nlp, test)
  

    print([intents.get_weight(token.lemma_) for token in message.tokens])
    print([token.dep_ for token in message.tokens])
    intent = natural_processing.process(message)


    print("para a mensagem: (", test, ") foi detectado o seguinte intent:")
    print("intent", "lex", "stc", "ent", "ctx", "total")
    for i in intent:
        print(i.intent.name, i.lexical_score, i.structural_score, i.entity_score, i.context_score, i.total_score())


if __name__ == "__main__":
    test = input("qual test deseja rodar? ")
    if test == "1":
        regenerate_intents()
    elif test == "2":
        NLPTEST()