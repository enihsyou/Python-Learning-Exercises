import math


def checkio(input):
    data = [int(a) for a in input if a.isdecimal()]
    A = (data.pop(0), data.pop(0))
    B = (data.pop(0), data.pop(0))
    C = (data.pop(0), data.pop(0))
    D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    x = ((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) +
         (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1]) +
         (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / D
    y = ((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) +
         (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0]) +
         (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / D
    r = math.sqrt((A[0] - x) ** 2 + (A[1] - y) ** 2)
    print("(x{x:+g})^2+(y{y:+g})^2={r:g}^2".format(x = round(-x, 2), y = round(-y, 2),
                                                   r = round(r, 2)))

checkio("(3,7),(6,9),(9,7)")
checkio("(2,2),(6,2),(2,6)")
