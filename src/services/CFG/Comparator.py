from ..levenshtein import distance as levenshtein


def compare_rules(rule1, rule2):
    rhs1 = [symbol.name for symbol in rule1.rhs]
    rhs2 = [symbol.name for symbol in rule2.rhs]

    set1 = set(rhs1)
    set2 = set(rhs2)

    intersection = set1.intersection(set2)

    similarity1 = len(intersection) / len(set1)
    similarity2 = len(intersection) / len(set2)

    return (similarity1 + similarity2) / 2


def compare_ordened_rules(rule1, rule2):
    rhs1 = [symbol.name for symbol in rule1.rhs]
    rhs2 = [symbol.name for symbol in rule2.rhs]

    return 1 - levenshtein(rhs1, rhs2) / max(len(rhs1), len(rhs2))