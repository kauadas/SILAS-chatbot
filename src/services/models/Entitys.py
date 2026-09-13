import pickle

class EntitysGroup:
    def __init__(self, entitys):
        
        self.entitys = entitys

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename) -> "EntitysGroup":
        with open(filename, "rb") as f:
            return pickle.load(f)

class Entity:
    def __init__(self, name, extract_method, type):
        self.name = name
        self.extract_method = extract_method
        self.type = type