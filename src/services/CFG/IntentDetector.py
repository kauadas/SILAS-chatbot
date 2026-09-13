from .Comparator import compare_rules, compare_ordened_rules
from .Grammar import Grammar
from .Symbol import Symbol

def compare_rules_with_grammar(rule, grammar, lhs):
    candidates = []
    lhs = Symbol(lhs)
    for grammar_rule in grammar.get_rules_by_lhs(lhs):
        similarity1 = compare_ordened_rules(rule, grammar_rule)
        similarity2 = compare_rules(rule, grammar_rule)
        candidates.append((similarity1 + similarity2) / 2)

    if not candidates:
        return 0

    candidate = max(candidates)
    return candidate