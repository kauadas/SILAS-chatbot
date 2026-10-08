from .Informations import Template, Entity
import regex as re

entity_pattern = re.compile(r"\{(.*?)\}")



class Corpus:
    def __init__(self, templates: dict):
        
        self.templates = {}

        for key in templates.keys():
            self.templates[key] = []
            for template in templates[key]:
                entities = entity_pattern.findall(template)
                entities = [Entity(name=entity) for entity in entities]
                self.templates[key].append(Template(template, entities))

    def __repr__(self):
        return f"Corpus(Structures={len(self.Structures)}, templates={len(self.templates)})"


if __name__ == "__main__":
    corpus = {
    "templates": {
        "location": ["em {location}", "na região de {location},", "na cidade de {location}"],
        "temperature": ["a temperatura é de {temperature} graus", "a temperatura está em {temperature} graus", "a temperatura é de {temperature}°C"],
        "humidity": ["a umidade é de {humidity}%", "a umidade está em {humidity}%", "a umidade relativa do ar é de {humidity}%"]
    }
    }

    
    intent = Corpus(corpus["templates"])

    for key in intent.templates.keys():
        print(f"Templates for {key}:")
        for template in intent.templates[key]:
            print(f"  - {template.text} (entities: {template.entitys})")


    