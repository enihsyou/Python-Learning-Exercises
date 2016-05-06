import re


def longest_palindromic(text):
    pattern = ''
    text_len = len(text)
    longest = ''
    for i in range(text_len):
        det = ''
        for j in range(i):
            det += '\\' + str(i - j)
        pattern = r'(.)' * (i) + '.?' + det
        # print(pattern)
        search = re.search(pattern, text)
        if search:
            # print(search.group(0))
            longest = search.group(0)
            # print()
    print(longest)
    return longest


# if __name__ == '__main__':
#     assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
#     assert longest_palindromic("abacada") == "aba", "The First"
#     assert longest_palindromic("aaaa") == "aaaa", "The A"

longest_palindromic("artrartrt")
longest_palindromic("abacada")
longest_palindromic("aaaa")
longest_palindromic("abba")
