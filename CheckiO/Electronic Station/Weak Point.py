# def weak_point(input):
#     minr = [sum(add) for add in input]
#     minc = [sum([data[i] for data in input]) for i in range(len(input[0]))]
#     return [minr.index(min(minr)), minc.index(min(minc))]


def weak_point(matrix):
    row_sums = list(map(sum, matrix))
    column_sums = list(map(sum, list(zip(*matrix))))
    return row_sums.index(min(row_sums)), column_sums.index(min(column_sums))


weak_point([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
