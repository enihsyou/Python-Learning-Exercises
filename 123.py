# import subprocess
#
# p = subprocess.Popen('D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise_scale --scale_ratio 1.6 --noise_level 2', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
# for line in p.stdout.readlines():
#     print(line)



# a = b'\x95\xcf\x8a\xb7\x82\xc9\x90\xac\x8c\xf7\x82\xb5\x82\xdc\x82\xb5\x82\xbd\r\n'
# print(a.decode('gbk'))
# print(a.decode('shift_jis'))

import os

# b = os.popen('D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise --noise_level 2').readlines()
# b = ['曄姺偵惉岟偟傑偟偨\n']
# print(bytes(b[0].encode('gbk')).decode('shift-jis'))

# b = r'D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe'
# input_path = r'-i D:\test\001.jpg'
# mode = r'-m noise'
# noise_level = r'--noise_level 2'
# c = [b, input_path, mode, noise_level]
#
# print(" ".join(c))
# 'D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise --noise_level 2'
import random

import subprocess, shlex

#
# command_line = input()
# args = shlex.split(command_line)
# print(args)
# p = subprocess.Popen(args)
# print(p)
# subprocess.Popen('D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise --noise_level 2', shell = True, stdout = subprocess.PIPE).stdout.read()
# os.system('D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m scale -s 0.5')
# os.popen('D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise_scale --scale_ratio 1.6 --noise_level 2')
# print(subprocess.Popen("D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m scale -s 0.5", shell = True, stdout = subprocess.PIPE).stdout.read())

# print(subprocess.Popen(r"waifu2x-caffe-cui.exe -i 001.jpg", shell = True, stdout = subprocess.PIPE).stdout.read())
# os.popen(r"D:\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\002.jpg")


# subprocess.call('ls')
# a = os.popen(r"D:\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\002.jpg")
# print(a.read())



# import os, sys
#
# # using command mkdir
# a = 'mkdir nwdir'
#
# b = os.popen(a, 'r', 1)
#
# print(b)

# import ctypes
# drive = "D:\\"
# folder = "test"
# image = "001.jpg"
# image_path = os.path.join(drive, folder, image)
# print(image_path)
# SPI_SETDESKWALLPAPER = 20
# SPIF_UPDATEINIFILE = 0
# SystemParametersInfo = ctypes.windll.user32.SystemParametersInfoW
# r'D:\test\001.jpg'
# SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE)
#
#
# import time
#
#
# class UnionFind1:
#     def __init__(self, size):
#         # 負の値はルート (集合の代表) で集合の個数
#         # 正の値は次の要素を表す
#         self.table = [-1 for _ in range(size)]
#
#     # 集合の代表を求める
#     def find(self, x):
#         while self.table[x] >= 0:
#             x = self.table[x]
#         return x
#
#     # 併合
#     def union(self, x, y):
#         s1 = self.find(x)
#         s2 = self.find(y)
#         if s1 != s2:
#             if self.table[s1] >= self.table[s2]:
#                 # 小さいほうが個数が多い
#                 self.table[s1] += self.table[s2]
#                 self.table[s2] = s1
#             else:
#                 self.table[s2] += self.table[s1]
#                 self.table[s1] = s2
#             return True
#         return False
#
#     def union_bad(self, x, y):
#         s1 = self.find(x)
#         s2 = self.find(y)
#         if s1 != s2:
#             if self.table[s1] > self.table[s2]:
#                 # 小さいほうが個数が多い
#                 self.table[s1] += self.table[s2]
#                 self.table[s2] = s1
#             else:
#                 self.table[s2] += self.table[s1]
#                 self.table[s1] = s2
#             print(self.table)
#             return True
#         return False
#
#
# def test_union(func, data, size):
#     a = time.clock()
#     for x, y in data:
#         func(x, y)
#     print(time.clock() - a)
#
# for size in [10]:
#     data = [(random.randint(0, size - 1), random.randint(0, size - 1)) for _ in range(size)]
#     print(data)
#     print(size)
#     s2 = UnionFind1(size)
#     s3 = UnionFind1(size)
#     test_union(s2.union, data, size)
#     test_union(s3.union_bad, data, size)


import random


def make_grid(size):
    table = [[] for _ in range(size * size)]
    for x in range(size):
        for y in range(size):
            n = y * size + x
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if random.random() < 0.34:
                    x1 = x + dx
                    y1 = y + dy
                    if 0 <= x1 < size and 0 <= y1 < size:
                        n1 = y1 * size + x1
                        if n1 not in table[n]:
                            # 接続
                            table[n].append(n1)
                            table[n1].append(n)
    return table


make_grid(2)


class DFS:
    def __init__(self, adjacent):
        self.adjacent = adjacent
        self.table = [0] * len(adjacent)
        self.count = [0]
        self.group = 0
        # 連結された頂点をたどって同じ番号を付ける
        for i in range(len(adjacent)):
            if self.table[i] == 0:
                self.group += 1
                self.count.append(0)
                self.dfs(i)

    # 深さ優先探索
    def dfs(self, node):
        # print(self.table[:4])
        # print(self.table[4:8])
        # print(self.table[8:12])
        # print(self.table[12:])
        # print(self.count)
        # print(self.group)
        if self.table[node] == 0:
            self.table[node] = self.group
            self.count[self.group] += 1
            for x in self.adjacent[node]:
                self.dfs(x)

    # 頂点が属する番号を返す
    def find(self, x):
        return self.table[x]

    # 部分集合とその要素数を返す
    def subsetall(self):
        return [(x, self.count[x]) for x in range(1, len(self.count))]


# 頂点の番号を表示する
def print_grid(s, size):
    for y in range(size):
        for x in range(size):
            print("%3d" % s.find(y * size + x), end = '')
        print()


a = make_grid(20)
s = DFS(a)
print(s.subsetall())
print_grid(s, 20)


class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    # 部分集合とその要素数を返す
    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a


# test
# a = make_grid(20)
s = UnionFind(20 * 20)
for x in range(20 * 20):
    for n in a[x]:
        if x < n: s.union(x, n)
print(s.subsetall())
print_grid(s, 20)

