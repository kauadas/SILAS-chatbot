
from .Symbol import Symbol
from .Ruler import Rule


def Simplify(rule_, rules):
    length = len(rule_.rhs)
    rhs1 = [symbol.name for symbol in rule_.rhs]
    for rule in rules:
        length_rule = len(rule.rhs)
        rhs2 = [symbol.name for symbol in rule.rhs]
        if length >= length_rule:
            for i in range(length - length_rule + 1):
                if rhs1[i:i + length_rule] == rhs2:
                    new_symbol = Symbol(rule.lhs.name)
                    new_symbol.tree = rule_.rhs[i:i + length_rule]
                    rule_.rhs = rule_.rhs[:i] + [new_symbol] + rule_.rhs[i + length_rule:]
                    return Simplify(rule_, rules)

    return rule_
        

def Parse(tokens,pos, deps):
    rule = []

    rule.append(Symbol("S"))
    rule.append([])
    for token, pos_tag, dep_tag in zip(tokens, pos, deps):
        if pos_tag == "PUNCT":
            continue
        rule[1].append(Symbol(f"{pos_tag}_{dep_tag}", True, token))

    rule = Rule(rule[0], rule[1])

    return rule