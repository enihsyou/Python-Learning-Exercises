from math import sqrt

y1 = 10 # sqrt(y)
while 1:
    y = y1 * y1
    x = y - 100
    z = y + 68
    if int(sqrt(z)) ** 2 == z:
        print(x)
        break
    else:
        y1 += 1
# x = 156
