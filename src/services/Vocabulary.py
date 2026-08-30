

class Vocabulary:
    def __init__(self, words):
        self.words = words

    def normalize(self, word):
        possibilities = []
        if word.lower() in self.words:
            return word.lower()
        
        for w in self.words:
            original_word = set(word.lower())
            normalized_word = set(w.lower())

            intersection = (original_word & normalized_word)

            similarity1 = len(intersection) / len(original_word)
            similarity2 = len(intersection) / len(normalized_word)

            similarity = (similarity1 + similarity2) / 2

            possibilities.append((w, similarity))


        print(sorted(possibilities, key=lambda x: x[1], reverse=True)[:3])
        return max(possibilities, key=lambda x: x[1])[0]

    def normalize_phrase(self, phrase):
        return " ".join([self.normalize(word) for word in phrase.split(" ")])