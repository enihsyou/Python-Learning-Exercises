from math import hypot as y
import itertools as o


def golf(t):
    return min([sum(y(i[0] - j[0], i[1] - j[1]) for i, j in list(zip(u, u[1:]))) + y(*u[0]) for u in o.permutations(t)])


print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}))


