# modelo que armazena probabilidades de transição, simbolos, etc.


class Model:
    def __init__(self, name: str):
        self.name = name
        self.structures = {} # chunk --> chunk
        self.structures_probabilities = {} # chunk:index --> chunk:index
        self.templates = {} # chunk --> [templates]

        
        
        
        