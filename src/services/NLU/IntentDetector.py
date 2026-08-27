from .models.Intents import IntentsGroup

class IntentCandidate:
    def __init__(self, intent):
        self.intent = intent
        self.lexical_score = 0
        self.structural_score = 0
        self.entity_score = 0
        self.context_score = 0

    def total_score(self):
        return self.lexical_score + self.structural_score + self.entity_score + self.context_score

class StructureMatcher:

    def _levenshtein(self, s1, s2):
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

    def similarity(self, message, structure):
        message_structure = message.deps

        if not message_structure or not structure:
            return 2

        distance = self._levenshtein(message_structure, structure)
        
        similarity = 1 - (distance / max(len(message_structure), len(structure)))
        return similarity

    def compare(self, message, structures):
        candidates = []
        for structure in structures:
            similarity = self.similarity(message, structure)
            candidates.append(similarity)

        candidate = max(candidates)
        return candidate
    
class IntentDetector:
    def __init__(self, intents: IntentsGroup):
        self.intents = intents

    def phrase_matcher(self, message, phrase):
        message_lemmas = set(message.lemmas)
        phrase_lemmas = set(phrase)

        if not message_lemmas or not phrase_lemmas:
            return 0.0

        intersection = message_lemmas.intersection(phrase_lemmas)


        phrase_similarity = len(intersection) / len(phrase_lemmas)

        message_similarity = len(intersection) / len(message_lemmas)


        similarity = (phrase_similarity + message_similarity) / 2

        return similarity

    def lexical_similarity(self, message, intent):
        candidates = []

        for phrase in intent.lemmas:
            similarity = self.phrase_matcher(message, phrase)
            #print(f"Similarity: {similarity}")
            candidates.append(similarity)
                
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
            candidate.structural_score = StructureMatcher().compare(message, candidate.intent.deps)

        candidates = sorted(candidates, key=lambda x: x.total_score(), reverse=True)

        return candidates[:3]
                