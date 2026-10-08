from dataclasses import dataclass

@dataclass
class Template:
    text: str
    entitys: list

@dataclass
class Entity:
    name: str
    value = None