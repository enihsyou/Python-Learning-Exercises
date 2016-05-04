"""
File name: Boolean Algebra
Reference: https://checkio.org/mission/boolean-algebra/
Time: ${YEAR}-${MONTH}-${DAY}
By: enihsyou
"""


def boolean(x, y, operation):
    func = {
        "conjunction": lambda a, b: a & b,
        "disjunction": lambda a, b: a | b,
        "implication": lambda a, b: (not a) | b,
        "exclusive": lambda a, b: a ^ b,
        "equivalence": lambda a, b: not(a ^ b)
    }
    return func[operation](x, y)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
