import random

class MarkovChain:
    def __init__(self, grammar, nlp):
        self.grammar = grammar
        self.nlp = nlp
        self.model = {}
        self.symbols = {}

    def build_model(self, corpus, n=1):
        corpus = corpus.lower().split()
        for i in range(len(corpus) - n):
            key = " ".join(corpus[i:i + n])
            value = " ".join(corpus[i + n:i + n + 1])

            doc = self.nlp(value)
            symbols = [f"{v.pos_}_{v.dep_}" for v in doc]

            for symbol, word in zip(symbols, doc):
                x = self.symbols.get(symbol, [])
                word = str(word)
                if word not in x:
                    x.append(word)

                self.symbols[symbol] = x


            if not key in self.model:
                self.model[key] = {}

            str_value = str(value)
            if not str_value in self.model[key]:
                
                self.model[key][str_value] = 1

            else:
                
                self.model[key][str_value] += 1

        return self.model

    def generate(self, seed, n=1, length=80):
        words = seed.lower().split()

        for _ in range(length):
            key = " ".join(words[-n::])

            if key not in self.model:
                print(key)
                break

            possible = list(self.model[key].keys())
            weights = list(self.model[key].values())

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
    markov_chain.build_model(corpse, 3)
    print(markov_chain.symbols)
    

    print(markov_chain.generate("o pequeno dinossauro", 3))
