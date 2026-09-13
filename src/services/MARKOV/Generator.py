import random

class MarkovChain:
    def __init__(self, grammar, nlp):
        self.grammar = grammar
        self.nlp = nlp
        self.models = {}
        self.symbols = {}

    def build_model(self,name: str, corpus, n=1):
        corpus = corpus.lower().split()
        model = {}
        for i in range(len(corpus) - n):
            key = " ".join(corpus[i:i + n])
            value = " ".join(corpus[i + n:i + n + 1])

            doc = self.nlp(value)
            symbols = [f"{v.pos_}" for v in doc]

            for symbol, word in zip(symbols, doc):
                x = self.symbols.get(symbol, [])
                word = str(word)
                if word not in x:
                    x.append(word)

                self.symbols[symbol] = x


            if not key in model:
                model[key] = {}

            str_value = str(value)
            if not str_value in model[key]:
                
                model[key][str_value] = 1

            else:
                
                model[key][str_value] += 1

        self.models[name] = model
        return self.models[name]

    def generate(self, model, seed, n=1, length=80):
        words = seed.lower().split()

        for _ in range(length):
            key = " ".join(words[-n::])

            if key not in self.models[model]:
                print(key)
                break

            possible = list(self.models[model][key].keys())
            weights = list(self.models[model][key].values())

            next_words = random.choices(possible, weights)[0]

            next_words = next_words.split()
            words.extend(next_words)

        return " ".join(words)


if __name__ == "__main__":
    import spacy

    with open("corpus.txt", "r") as f:
        corpse = f.read()
        
    
    nlp = spacy.load("pt_core_news_sm")
    markov_chain = MarkovChain(None, nlp)
    markov_chain.build_model("corpus", corpse, 3)
    print(markov_chain.symbols)
    

    print(markov_chain.generate("corpus", "o pequeno dinossauro", 3))
