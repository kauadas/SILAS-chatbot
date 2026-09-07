
from .Symbol import Symbol
from .Ruler import Rule


def Simplify(rule_, rules):
    length = len(rule_.rhs)
    for rule in rules:
        length_rule = len(rule.rhs)
        if length >= length_rule:
            for i in range(length - length_rule + 1):
                if rule_.rhs[i:i + length_rule] == rule.rhs:
                    rule_.rhs = rule_.rhs[:i] + [rule.lhs] + rule_.rhs[i + length_rule:]
                    return Simplify(rule_, rules)

    return rule_
        

def Parse(pos, deps, grammar_symbols):
    rule = []

    rule.append(grammar_symbols["S"])
    rule.append([])
    for pos_tag, dep_tag in zip(pos, deps):
        if pos_tag == "PUNCT":
            continue
        rule[1].append(grammar_symbols.get(f"{pos_tag}_{dep_tag}", Symbol(f"{pos_tag}_{dep_tag}")))

    rule = Rule(rule[0], rule[1])

    return rule