import spacy




nlp = spacy.load("pt_core_news_sm")



def regenerate_intents():
    from services.models.Intents import IntentsGroup, Intent
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
    from services.models.Intents import IntentsGroup, Intent
    from services.CFG.Grammar import Grammar
    from services.CFG.Parser import Parse
    from services.CFG.Symbol import Symbol
    from services.preprocessing.processedText import ProcessedText

    grammar = Grammar([])


    intents = IntentsGroup.load("intents.pkl")
    intents.vocab = []
    intents.gen_vocab()

    for intent in intents.intents:
            for phrase in intent.phrases:
                message = ProcessedText(nlp, phrase)
                S = intent.name
                S = Symbol(S)
                rule = Parse(S, message.tokens, message.tags, message.deps)
                grammar.add_rule(rule)

    print(len(intents.intents))


    natural_processing = NaturalProcessing(intents, None, grammar)
    test = input(" >> ")
    message = ProcessedText(nlp, test)
  

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
    from services.preprocessing.processedText import ProcessedText
    

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
    
    
    message = ProcessedText(nlp, test)

    rule = Parse(S, message.tokens, message.tags, message.deps)

    print(f"{rule.lhs.name} -> {" + ".join([symbol.name for symbol in rule.rhs])}")

    rule = Simplify(rule, grammar.rules)

    print(f"{rule.lhs.name} -> {" + ".join([symbol.name for symbol in rule.rhs])}")
    print("Árvore de derivação:")
    for symbol in rule.rhs:
        if symbol.tree:
            print(f"{symbol.name} -> {" + ".join([s.name for s in symbol.tree])}")
        else:
            print(f"{symbol.name} (terminal)")

def GFCTEST2():
    
    from services.CFG.Grammar import Grammar
    from services.CFG.Symbol import Symbol
    from services.CFG.Ruler import Rule
    from services.CFG.Parser import Parse
    from services.CFG.Comparator import compare_ordened_rules, compare_rules
    from services.preprocessing.processedText import ProcessedText
    from services.models.Intents import IntentsGroup

    intents = IntentsGroup.load("intents.pkl")
    intents.vocab = []
    intents.gen_vocab()

    grammar = Grammar([])


    for intent in intents.intents:
        for phrase in intent.phrases:
            message = ProcessedText(nlp, phrase)
            S = intent.name
            S = Symbol(S)
            rule = Parse(S, message.tokens, message.tags, message.deps)
            grammar.add_rule(rule)

    test = input("digite uma frase para testar a gramática: ")
    message = ProcessedText(nlp, test)
    rule = Parse(Symbol("S"), message.tokens, message.tags, message.deps)

    candidates = {}
    for grammar_rule in grammar.rules:
        similarity1 = compare_ordened_rules(rule, grammar_rule)
        similarity2 = compare_rules(rule, grammar_rule)
        max_candidate = candidates.get(grammar_rule.lhs.name, (0, 0, 0))
        if (similarity1 + similarity2) / 2 > max_candidate[0]:
            candidates[grammar_rule.lhs.name] = ((similarity1 + similarity2) / 2, similarity1, similarity2)

    candidates = sorted(candidates.items(), key=lambda x: x[1][0], reverse=True)
    for candidate in candidates[:3]:
        print(f"Intent: {candidate[0]}, Similarity: {candidate[1][0]}, Similarity1: {candidate[1][1]}, Similarity2: {candidate[1][2]}")



def complete_test():
    from services.NLP.NaturalProcessing import NaturalProcessing
    from services.models.Intents import IntentsGroup, Intent

    from services.CFG.Grammar import Grammar
    from services.CFG.Symbol import Symbol
    from services.CFG.Ruler import Rule
    from services.CFG.Parser import Parse
    from services.CFG.Comparator import compare_ordened_rules, compare_rules

    from services.preprocessing.processedText import ProcessedText


    intents = IntentsGroup.load("intents.pkl")
    intents.vocab = []
    intents.gen_vocab()

    grammar = Grammar([])

    for intent in intents.intents:
        for phrase in intent.phrases:
            message = ProcessedText(nlp, phrase)
            S = intent.name
            S = Symbol(S)
            rule = Parse(S, message.tokens, message.tags, message.deps)
            grammar.add_rule(rule)


    print(len(intents.intents))


    from services.preprocessing.processedText import ProcessedText
    natural_processing = NaturalProcessing(intents, None)
    test = input(" >> ")
    message = ProcessedText(nlp, test)

    print([intents.get_weight(token.lemma_) for token in message.tokens])
    print([token.dep_ for token in message.tokens])
    intents = natural_processing.process(message)


if __name__ == "__main__":
    test = input("qual test deseja rodar? ")
    if test == "1":
        regenerate_intents()
    elif test == "2":
        NLPTEST()
    elif test == "3":
        CFGTEST()
    elif test == "4":
        GFCTEST2()
    elif test == "5":
        complete_test()