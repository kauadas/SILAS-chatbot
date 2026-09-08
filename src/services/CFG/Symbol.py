
class Symbol:
    def __init__(self, name, terminal=False, value=None):
        self.name = name
        self.terminal = terminal
        self.value = value
        self.tree = []

    def set_value(self, value):
        self.value = value
        self.terminal = True

    def __repr__(self):
        return f"Symbol({self.name}, terminal={self.terminal}, value={self.value})"

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.name == other.name and self.terminal == other.terminal and self.value == other.value
        return False

    def basic_eq(self, other):
        if isinstance(other, Symbol):
            return self.name == other.name
        return False

def compare_symbols(symbol1, symbol2):
    if symbol1.name != symbol2.name:
        return False

    return True