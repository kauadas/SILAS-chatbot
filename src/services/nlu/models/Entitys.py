import pickle

class EntitysGroup:
    def __init__(self, entitys):
        self.entitys = entitys

class Entity:
    def __init__(self, name, search_pattern, type):
        self.name = name
        self.search_pattern = search_pattern
        self.type = type