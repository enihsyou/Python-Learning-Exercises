def first_word(word1, word2, likeness):
    if word1[0] == word2[0]:
        return likeness + 10
    else:
        return likeness


def last_word(word1, word2, likeness):
    if word1[-1] == word2[-1]:
        return likeness + 10
    else:
        return likeness


def length_comparison(word1, word2, likeness):
    if len(word1) <= len(word2):
        return likeness + 30 * (len(word1) / len(word2))
    else:
        return likeness + 30 * (len(word2) / len(word1))


def letter_comparison(word1, word2, likeness):
    letter1 = {w for w in word1}
    letter2 = {w for w in word2}
    return likeness + 50 * (len(letter1 & letter2) / len(letter1 | letter2))


def find_word(messages):
    message = [item for item in messages.lower().split()]
    message.reverse()
    for item in message[:]:
        if not item[-1].isalpha():
            message[message.index(item)] = item[:len(item) - 1]
    print(message)
    likeness = []
    for i in range(len(message)):
        lst = []
        # for j in range(i + 1, len(message)):
        for j in range(len(message)):
            coefficient = 0
            coefficient = first_word(message[i], message[j], coefficient) + \
                          last_word(message[i], message[j], coefficient) + \
                          length_comparison(message[i], message[j], coefficient) + \
                          letter_comparison(message[i], message[j], coefficient)
            lst.append(coefficient)
        likeness.append(lst)
    print(likeness)
    likeness_sum = list(map(sum, likeness))
    print(likeness_sum)
    print(likeness_sum.index(max(likeness_sum)))
    print(message[likeness_sum.index(max(likeness_sum))])
    return message[likeness_sum.index(max(likeness_sum))]
    # print(max(likeness, key = sum(likeness[i] for i in range(len(likeness)))))


find_word(u"Beard and Bread")
