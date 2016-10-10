from fractions import Fraction
from math import factorial

e = 0
for num in (Fraction(1, factorial(n)) for n in range(100)):
    if num < 10 ** -6:
        print("e ≈ %.6f" % float(e))
        break
    e += num
