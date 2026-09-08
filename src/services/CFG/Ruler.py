
class Rule:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __eq__(self, value):
        if not isinstance(value, Rule):
            return False

        value = [symbol.name for symbol in value.rhs]
        for symbol in self.rhs:
            if symbol.name not in value:
                return False
        return True
