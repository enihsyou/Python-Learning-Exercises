import math

number = int(input("输入一个整数"))

for i in range(int(math.sqrt(number)) + 1):
    if i * i == number:
        print("输入的{}是{}的平方".format(number, i))
        break
else:
    print("输入的{}不是另一个数的平方".format(number))
