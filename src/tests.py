import spacy

nlp = spacy.load("pt_core_news_sm")



def regenerate_intents():
    from services.NLP.models.Intents import IntentsGroup, Intent
    import json
    
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


def CFGTEST():
    from services.CFG.Grammar import Grammar
    from services.CFG.Symbol import Symbol
    from services.CFG.Ruler import Rule
    from services.CFG.Parser import Parse, Simplify
    from services.preprocessing.message import Message
    

    grammar = Grammar([])

    S = Symbol("S")
    VR = Symbol("VERB_ROOT")
    VN = Symbol("VN")
    NO = Symbol("NOUN_obj")
    DET = Symbol("DET_det")
    PN = Symbol("PRON_nsubj")

    grammar.add_symbol(S)
    
    grammar.add_rule(Rule(VN, [VR, DET, NO]))
    for rule in grammar.rules:
        print(f"{rule.lhs.name} -> {" + ".join([symbol.name for symbol in rule.rhs])}")
    

    test = input("digite uma frase para testar a gramática: ")
    
    
    message = Message(nlp, test)

    rule = Parse(message.tokens, message.tags, message.deps)

    print(f"{rule.lhs.name} -> {" + ".join([symbol.name for symbol in rule.rhs])}")

    rule = Simplify(rule, grammar.rules)

    print(f"{rule.lhs.name} -> {" + ".join([symbol.name for symbol in rule.rhs])}")
    print("Árvore de derivação:")
    for symbol in rule.rhs:
        if symbol.tree:
            print(f"{symbol.name} -> {" + ".join([s.name for s in symbol.tree])}")
        else:
            print(f"{symbol.name} (terminal)")


    

if __name__ == "__main__":
    test = input("qual test deseja rodar? ")
    if test == "1":
        regenerate_intents()
    elif test == "2":
        NLPTEST()
    elif test == "3":
        CFGTEST()