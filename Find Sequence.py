def horizontally(data):
    for i in range(len(data)):
        yield data[i]


def vertically(data):
    data = list(zip(*data))
    for i in range(len(data)):
        yield list(data[i])


def main_diagonally(data):
    for j in range(len(data)):
        lst = []
        for i in range(len(data) - j):
            lst.append(data[j + i][i])
        yield lst
    for j in range(1, len(data)):
        lst = []
        for i in range(len(data) - j):
            lst.append(data[i][i + j])
        yield lst


def sub_diagonally(data):
    for j in range(len(data)):
        lst = []
        for i in range(j + 1):
            lst.append(data[i][j - i])
        yield lst
    for j in range(1, len(data)):
        lst = []
        for i in range(len(data) - j):
            lst.append(data[j + i][len(data) - i - 1])
        yield lst


# 0,0
# 0,1 1,0
# 0,2 1,1 2,0

# 1,6 2,5 3,4 4,3 5,2

def check(data):
    for item in data:
        if len(item) >= 4:
            for i in range(len(item) - 4 + 1):
                if len(set(item[i:i + 4])) == 1:
                    return True
    return False


def checkio(data):
    hor = list(horizontally(data))
    ver = list(vertically(data))
    sub = list(sub_diagonally(data))
    main = list(main_diagonally(data))
    return check(hor) or check(ver) or check(sub) or check(main)




# def checkio(matrix, l = 3):
#     q = range(len(matrix))
#     ls = lambda x: len(set(x))
#     for i in q:
#         for j in q:
#             if i + l in q and ls([matrix[i + n][j] for n in range(4)]) == 1:
#                 return True
#             if j + l in q and ls([matrix[i][j + n] for n in range(4)]) == 1:
#                 return True
#             if j + l in q and i + l in q and ls([matrix[i + n][j + n] for n in range(4)]) == 1:
#                 return True
#             if j - l in q and i + l in q and ls([matrix[i + n][j - n] for n in range(4)]) == 1:
#                 return True
#     return False


print(checkio([
    [1, 2, 1, 1, 3],
    [1, 1, 4, 1, 3],
    [2, 3, 1, 6, 2],
    [1, 7, 2, 1, 4],
    [1, 3, 5, 6, 1]
]))
