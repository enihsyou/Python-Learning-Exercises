import itertools as o
from math import hypot as y

golf = lambda t: min(sum(y(a - c, b - d) for (a, b), (c, d) in zip(u, u[1:])) + y(*u[0]) for u in o.permutations(t))

print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}))
