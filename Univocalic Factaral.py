# 1st
# a_factaral = lambda x: (x > 1 and x * a_factaral(x - 1)) + (x < 2 and 1)

# 2nd
a_factaral = lambda x: (x and x * a_factaral(x - 1)) + (x < 1 and 1)

# 3rd
#a_factaral = lambda x: (x and x * a_factaral(x - 1)) + (x < 1 and 1)
print(a_factaral(2))
print(a_factaral(10))
print(a_factaral(5))
# a_factaral = lambda n: (n > 0 and ((n == 0 and 1) + n) * a_factaral(n - 1)) + (n == 0 and 1)
# print(a_factaral(100))
