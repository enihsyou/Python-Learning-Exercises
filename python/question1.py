def ten2(number, base):
    result = []
    while number:
        number, a = divmod(number, base)
        result.append(str(a))
    result.reverse()
    return ''.join(result)


for i in range(100, 1000):
    if ten2(i, 7) == ten2(i, 9)[::-1]:
        print(i)

# i = 248
