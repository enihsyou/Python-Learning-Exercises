import random


def rotate(data, i):
    return [data[i % 3], data[(i + 1) % 3], data[(i + 2) % 3]]


def filp(data):
    return [data[2], data[1], data[0]]


def get_chain(data):
    data = data
    used = []
    chain = []
    for i in range(6 * 5 * 4 * 3 * 2):
        used.append(0)
        chain.append(data[0])

        for k in range(6):
            for j in range(6):
                j = random.randint(0, 5)
                if j not in used:
                    if data[j][0] == chain[-1][2]:
                        used.append(j)
                        if random.random() > 0.5:
                            chain.append(data[j])
                        else:
                            chain.append([data[j][0], data[j][2], data[j][1]])
                    elif data[j][1] == chain[-1][2]:
                        used.append(j)
                        if random.random() > 0.5:
                            chain.append(rotate(data[j], 1))
                        else:
                            chain.append([data[j][1], data[j][0], data[j][2]])
                    elif data[j][2] == chain[-1][2]:
                        used.append(j)
                        if random.random() > 0.5:
                            chain.append(rotate(data[j], 2))
                        else:
                            chain.append([data[j][2], data[j][1], data[j][0]])
                            # print(chain)
        if len(chain) != 6 or chain[0][0] != chain[-1][-1]:
            # print(chain)
            used = []
            chain = []
            if random.random() > 0.5:
                data[0] = filp(data[0])
            else:
                data[0] = rotate(data[0], 1)
        else:
            print(chain)
            # print(used)
            yield chain


def checkio(data):
    lst = list(get_chain(data))
    # print(lst)
    a = [[c[i][1] for i in range(6)] for c in lst]
    b = list(map(lambda x: sum(x), a))
    # print(a)
    print(b)
    maxv = max(b) if b else 0
    print(maxv)
    return maxv


checkio([[9, 5, 1], [1, 5, 9], [9, 1, 5], [1, 9, 5], [5, 9, 1], [5, 1, 9]])
# checkio([[1, 4, 20], [3, 1, 5], [50, 2, 3],
#          [5, 2, 7], [7, 5, 20], [4, 7, 50]])
# checkio([[1, 10, 2], [2, 20, 3], [3, 30, 4],
#          [4, 40, 5], [5, 50, 6], [6, 60, 1]])
# checkio([[1, 2, 3], [2, 1, 3], [4, 5, 6],
#          [6, 5, 4], [5, 1, 2], [6, 4, 3]])
# checkio([[5, 9, 5], [9, 6, 9], [6, 7, 6],
#          [7, 8, 7], [8, 1, 8], [1, 2, 1]])
# checkio([[1, 2, 3], [2, 1, 3], [4, 5, 6], [6, 5, 4], [5, 1, 2], [6, 4, 3]])
