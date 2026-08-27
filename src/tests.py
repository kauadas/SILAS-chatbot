
def NLUTEST():
    from services.NLU.natural_processing import NaturalProcessing
    from services.NLU.models.Intents import IntentsGroup, Intent
    import spacy
    import json
    nlp = spacy.load("pt_core_news_sm")


    intents = []

    with open("/home/kstocker/Documentos/programação/SILAS chatbot/test.json", "r") as f:
        intentsjson = json.load(f)
        for intent in intentsjson["intents"]:
            intent = Intent(intent["name"], intent["phrases"], [], [], None, None)
            intents.append(intent)

    intents = IntentsGroup(intents)
    intents.process(nlp)

    print(len(intents.intents))

    from services.preprocessing.message import Message

    test = input(" >> ")

    natural_processing = NaturalProcessing(intents, None)
    message = Message(nlp, test)
    intent = natural_processing.process(message)

    print("para a mensagem: ", test, "foi detectado o seguinte intent:")
    for i in intent:
        print(i[0].name, i[1])


if __name__ == "__main__":
    NLUTEST()