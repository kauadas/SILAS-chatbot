from .Corpus import Corpus


class Generator:
    def __init__(self, corpus: Corpus):
        self.corpus = corpus

    def search_template(self, intent: str, entities: dict):
        if intent not in self.corpus.templates:
            raise ValueError(f"Intent '{intent}' not found in corpus.")

        templates = self.corpus.templates[intent]
        for template in templates:
            if all(entity.name in entities for entity in template.entitys):
                return template

        raise ValueError(f"No suitable template found for intent '{intent}' with provided entities.")

    def generate(self, intent: str, entities: dict):
        template = self.search_template(intent, entities)
        text = template.text
        for entity in template.entitys:
            if entity.name in entities:
                text = text.replace(f"{{{entity.name}}}", str(entities[entity.name]))
            else:
                raise ValueError(f"Entity '{entity.name}' not provided for intent '{intent}'.")

        return text
