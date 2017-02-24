import string

s = [9, 7, 8, 3, 2, 1, 5, 6]
print("former:      ", s)
# 把数组里的偶数二次方
print("After conversion: ", [i ** 2 if i % 2 == 0 else i for i in s])
