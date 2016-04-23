import math
import itertools as o

a = lambda a, i: math.hypot(a[0] - i[0], a[1] - i[1])


def golf(t):
    q = 99
    for u in o.permutations(t):
        b = sum(a(*c) for c in list(zip(u, u[1:]))) + a((0, 0), u[0])
        if b < q: q = b
    return q


print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}))
