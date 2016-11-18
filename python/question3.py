from math import sqrt

for i in range(1000, 10000):
    first2 = set(str(i)[:2])
    if len(first2) == 1:
        last2 = set(str(i)[2:])
        if len(last2) == 1 and not last2 & first2:
            if int(sqrt(i)) ** 2 == i:
                print(i)

# 7744
