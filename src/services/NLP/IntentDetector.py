from .models.Intents import IntentsGroup



class IntentCandidate:
    def __init__(self, intent):
        self.intent = intent
        self.lexical_score = 0
        self.structural_score = 0
        self.entity_score = 0
        self.context_score = 0

    def total_score(self):
        return self.lexical_score * 0.9 + self.structural_score * 0.1 + self.entity_score + self.context_score


def levenshtein(s1, s2):
        rows = len(s1) + 1
        cols = len(s2) + 1

        matrix = [[0] * cols for _ in range(rows)]

        for i in range(1, rows):
            matrix[i][0] = i

        for j in range(1, cols):
            matrix[0][j] = j

        for i in range(1, rows):
            for j in range(1, cols):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)

        return matrix[-1][-1]


class StructureMatcher:
    def similarity(self, message, structure):
        message_structure = message.deps

        if not message_structure or not structure:
            return 0

        distance = levenshtein(message_structure, structure)
        
        similarity = 1 - (distance / max(len(message_structure), len(structure)))
        return similarity

    def compare(self, message, structures):
        candidates = []
        for structure in structures:
            similarity = self.similarity(message, structure)
            candidates.append(similarity)

        if not candidates:
            return 0

        candidate = max(candidates)
        return candidate



class LexicalMatcher:
    def __init__(self, intents: IntentsGroup):
        self.intents = intents

    def lemma_similarity(self, message, phrase):
        message_lemmas = set(message.lemmas)
        phrase_lemmas = set(phrase)

        if not message_lemmas or not phrase_lemmas:
            return 0.0

        intersection = message_lemmas.intersection(phrase_lemmas)

        matched_weight = sum([self.intents.get_weight(lemma) for lemma in intersection])

        phrase_weight = sum([self.intents.get_weight(lemma) for lemma in phrase_lemmas])

        message_weight = sum([self.intents.get_weight(lemma) for lemma in message_lemmas])

        if phrase_weight == 0 or message_weight == 0:
            return 0

        phrase_similarity = matched_weight / phrase_weight

        message_similarity = matched_weight / message_weight


        similarity = (phrase_similarity + message_similarity) / 2

        return similarity

    def word_similarity(self, w1, w2):
        if w1 == w2:
            return 1

        distance = levenshtein(w1, w2)
        max_length = max(len(w1), len(w2))

        if max_length == 0:
            return 0

        similarity = 1 - (distance / max_length)
        return similarity


    def word_by_word_similarity(self, message, phrase):
        message_words = message.content.split(" ")
        phrase_words = phrase.split(" ")

        total_score = 0
        
        for phrase_word in phrase_words:
            best_similarity = 0
            for message_word in message_words:
                similarity = self.word_similarity(phrase_word, message_word)
                if similarity > best_similarity:
                    best_similarity = similarity

            total_score += best_similarity

        total_score /= len(phrase_words)

        return total_score
            
                


class IntentDetector:
    def __init__(self, intents: IntentsGroup):
        self.intents = intents
        self.structure_matcher = StructureMatcher()
        self.lexical_matcher = LexicalMatcher(intents)
        

    def lexical_similarity(self, message, intent):
        candidates = []

        for phrase, lemmas in zip(intent.phrases, intent.lemmas):
            similarity1 = self.lexical_matcher.lemma_similarity(message, lemmas)
            similarity2 = self.lexical_matcher.word_by_word_similarity(message, phrase)
            #print(f"Similarity: {similarity}")
            candidates.append((similarity1 + similarity2) / 2)

        if not candidates:
            return 0
        
        candidate = max(candidates)
        return candidate

    def detect_intent(self, message):
        candidates = []
        for intent in self.intents.intents:
            candidate = IntentCandidate(intent)
            lexical_similarity = self.lexical_similarity(message, intent)
            candidate.lexical_score = lexical_similarity
            candidates.append(candidate)

        for candidate in candidates:
            candidate.structural_score = self.structure_matcher.compare(message, candidate.intent.deps)

        candidates = sorted(candidates, key=lambda x: x.total_score(), reverse=True)

        return candidates[:3]
                