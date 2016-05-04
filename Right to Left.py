"""
File name: Right to Left
Reference: https://checkio.org/mission/right-to-left/
Time: 2016-05-04
By: enihsyou
"""


def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return ",".join([word.lower().replace('right', 'left') for word in phrases])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
