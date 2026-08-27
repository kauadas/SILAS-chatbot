from .models.Intents import IntentsGroup

class IntentDetector:
    def __init__(self, intents: IntentsGroup):
        self.intents = intents

    def _phrase_similarity(self, message, phrase):
        message_lemmas = set(message.lemmas)
        phrase_lemmas = set(phrase)

        if not message_lemmas or not phrase_lemmas:
            return 0.0

        intersection = message_lemmas.intersection(phrase_lemmas)
        
        phrase_similarity = len(intersection) / len(phrase_lemmas)
        message_similarity = len(intersection) / len(message_lemmas)


        similarity = (phrase_similarity + message_similarity) / 2

        return similarity

    def intent_detection_by_phrases(self, message, intent):
        candidates = []

        for phrase in intent.lemmas:
            similarity = self._phrase_similarity(message, phrase)
            #print(f"Similarity: {similarity}")
            candidates.append((intent, similarity))
                
        candidate = max(candidates, key=lambda x: x[1])
        return candidate

    def detect_intent(self, message):
        candidates = []
        for intent in self.intents.intents:
            candidates.append(self.intent_detection_by_phrases(message, intent))

        candidates = sorted(candidates, key=lambda x: x[1], reverse=True)
        return candidates[:3]
                