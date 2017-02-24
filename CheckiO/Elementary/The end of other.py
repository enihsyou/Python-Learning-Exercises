"""
File name: The end of other
Reference: https://checkio.org/mission/end-of-other/
Time: 2016-05-04
By: enihsyou
"""


def checkio(words_set):
    for a in words_set:
        words = words_set.copy()
        words.remove(a)
        for b in words:
            if a.endswith(b):
                return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
