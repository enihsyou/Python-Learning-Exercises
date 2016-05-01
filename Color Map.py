import itertools


def search(data, coor, index, rows, columns, colors, unexplored):
    x, y = coor
    if coor in unexplored:
        if data[x][y] == index:
            unexplored.remove(coor)
            for n, m in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if rows > x + n >= 0 and columns > y + m >= 0:
                    search(data, (x + n, y + m), index, rows, columns, colors, unexplored)
    if data[x][y] != index:
        color2 = colors[data[x][y]]
        if color2 in colors[index] and isinstance(color2, int):
            colors[index].remove(color2)
    return colors[index]


def color_map(region):
    rows = len(region)
    columns = len(region[0])
    unexplored = set(itertools.product(range(rows), range(columns)))  # 记录没有到过的点
    numbers = {k: [0, 1, 2, 3] for k in set(j for i in region for j in i)}  # 数据所拥有的数字种类
    index_p = []
    for index1, item1 in enumerate(region):
        for index2, item2 in enumerate(item1):
            # if maps[index1][index2] < 0: continue
            # if region[index1][index2] != index and region[index1][index2] not in index_p:
            if region[index1][index2] not in index_p:
                index = region[index1][index2]  # 当前主循环格子的数字值
                index_p.append(index)
            else:
                continue
            # unexplored.remove((index1, index2))
            numbers[index] = search(region, (index1, index2), index, rows, columns, numbers, unexplored)[0]
            print(numbers[index])
            print([(x, numbers[x] + 1) for x in numbers if numbers[x] != [0, 1, 2, 3]])
            print([(x, numbers[x]) for x in numbers])
            print()
    print([numbers[x] + 1 for x in numbers])
    return [numbers[x] + 1 for x in numbers]


# color_map(((7, 4, 4, 4,), (7, 0, 1, 5,), (7, 2, 3, 5,), (6, 6, 6, 5,),))
# color_map(((11, 0, 0, 0, 0, 0, 7, 0,), (0, 0, 0, 0, 0, 0, 7, 0,), (0, 0, 4, 4, 4, 0, 7, 0,), (0, 0, 0, 0, 0, 0, 0, 0,),
#            (0, 0, 1, 0, 1, 0, 0, 0,), (5, 5, 1, 2, 1, 6, 6, 0,), (0, 0, 1, 0, 1, 0, 0, 0,), (0, 0, 0, 0, 0, 0, 0, 0,),
#            (0, 0, 3, 3, 3, 0, 8, 0,), (0, 0, 10, 10, 9, 0, 8, 0,), (0, 0, 0, 10, 9, 9, 8, 0,),))

print()
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"


    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.")
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True


    assert checker(color_map, (
        (0, 0, 0),
        (0, 1, 1),
        (0, 0, 2),
    )), "Small"
    assert checker(color_map, (
        (0, 0, 2, 3),
        (0, 1, 2, 3),
        (0, 1, 1, 3),
        (0, 0, 0, 0),
    )), "4X4"
    assert checker(color_map, (
        (1, 1, 1, 2, 1, 1),
        (1, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 1),
        (1, 0, 0, 0, 1, 1),
        (1, 1, 0, 4, 3, 1),
        (1, 1, 1, 3, 3, 3),
        (1, 1, 1, 1, 3, 5),
    )), "6 pack"
