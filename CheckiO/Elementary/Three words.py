def checkio(words):
    return True if "".join(['1' if word.isalpha() else '0' for word in words.split()]).find('111') + 1 else False
    # word = words.split()
    # count = 0
    # for a in word:
    #     if a.isalpha():
    #         count += 1
    #     else: count = 0
    #     if count == 3:
    #         return True
    #     return True if count == 3 else False
    # return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
