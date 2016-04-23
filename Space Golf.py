import math
import itertools as o
def golf(t):
    q=99
    for u in o.permutations(t):
        a,b=(0,0),0
        for i in u:
            b+=math.hypot(a[0]-i[0],a[1]-i[1])
            a=i
        if b<q:q=b
    return q

print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}))
