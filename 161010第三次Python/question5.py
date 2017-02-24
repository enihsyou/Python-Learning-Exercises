pocket = set()  # 0:Red 1:White 2:Black
for i in range(4):
    for j in range(4):
        for k in range(7):
            if i + j + k != 8:
                continue
            pocket.add((i, j, k))
else:
    print("Total %d" % len(pocket))
    for item in pocket:
        print("Red:{}, White:{}, Black:{}".format(*item))
# Total 13
# Red:3, White:3, Black:2
# Red:1, White:1, Black:6
# Red:0, White:2, Black:6
# Red:0, White:3, Black:5
# Red:2, White:2, Black:4
# Red:2, White:0, Black:6
# Red:2, White:1, Black:5
# Red:2, White:3, Black:3
# Red:3, White:1, Black:4
# Red:3, White:0, Black:5
# Red:1, White:3, Black:4
# Red:3, White:2, Black:3
# Red:1, White:2, Black:5
