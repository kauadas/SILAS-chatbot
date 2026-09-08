from .Symbol import Symbol
from .Ruler import Rule
from .Parser import Parse

class Grammar:
    def __init__(self, rules):
        self.rules = rules
        self.symbols = {}
        

    def add_rule(self, rule):
        self.rules.append(rule)
        self.gen_symbols()

    def add_symbol(self, symbol):
        if symbol.name not in self.symbols:
            self.symbols[symbol.name] = Symbol(symbol.name)

    def gen_symbols(self):
        for rule in self.rules:
            self.add_symbol(rule.lhs)
            for symbol in rule.rhs:
                self.add_symbol(symbol)

        return self.symbols

    def is_valid(self, message, rule):
        tokens = message.tokens
        pos = message.tags
        deps = message.deps

        formation_rule = Parse(tokens, pos, deps)

        if rule == formation_rule:
            return True
        return False


    