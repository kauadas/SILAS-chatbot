from .models.Intents import IntentsGroup

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
            candidates.append((intent, similarity))
                
        candidate = max(candidates, key=lambda x: x[1])
        return candidate

    def detect_intent(self, message):
        candidates = []
        for intent in self.intents.intents:
            lexical_similarity = self.lexical_similarity(message, intent)

            candidates.append(lexical_similarity)

        candidates = sorted(candidates, key=lambda x: x[1], reverse=True)

        return candidates[:3]
                