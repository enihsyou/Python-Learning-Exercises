# def check(data, index_number, route_map, route_equal, current, i, j, q, w):
#     if (i + q) in range(len(data)) and (j + w) in range(len(data)) and data[i + q][j + w] == current:
#         if route_map[i + q][j + w]:
#             route_map[i][j] = route_map[i + q][j + w]
#             # while j - 1 in range(len(data)) and route_map[i][j - 1]:
#             #     j -= 1
#             #     route_map[i][j] = route_map[i][j + 1]
#             #     if i in range(1 , len(data[0]) - 1):
#             #         if route_map[i + 1][j]:
#             #             route_map[i + 1][j] = route_map[i][j + 1]
#             #         if route_map[i - 1][j]:
#             #             route_map[i - 1][j] = route_map[i][j + 1]
#             #     elif i == len(data):
#             #         if route_map[i - 1][j]:
#             #             route_map[i - 1][j] = route_map[i][j + 1]
#             #     elif i == 0:
#             #         if route_map[i + 1][j]:
#             #             route_map[i + 1][j] = route_map[i][j + 1]
#         else:
#             route_map[i + q][j + w] = route_map[i][j]
#
#
# def checkio(data):
#     i, j = 0, 0
#     current = data[i][j]
#     route_map = [[0 for i in range(len(data))] for j in range(len(data[0]))]
#     route_equal = {}
#     index_number = 1
#
#     route_map[i][j] = index_number
#
#     for i in range(len(data)):
#         for j in range(len(data[0])):
#             if data[i][j] == current:
#                 route_map[i][j] = index_number
#                 check(data, index_number, route_map, route_equal, current, i, j, 0, -1)
#                 check(data, index_number, route_map, route_equal, current, i, j, -1, 0)
#                 check(data, index_number, route_map, route_equal, current, i, j, 0, +1)
#                 check(data, index_number, route_map, route_equal, current, i, j, +1, 0)
#             else:
#                 index_number += 1
#
#     items = {item for i in range(len(route_map)) for item in route_map[i] if item != 0}
#     flat = [item for i in range(len(route_map)) for item in route_map[i]]
#
#     for i in range(len(data)):
#         print(route_map[i])
#     print(route_equal)
#     print(flat)
#     print(items)
#     # print(max(flat.count(item) for item in items))
#     result = {}
#     for item in items:
#         result[item] = flat.count(item)
#     print(result)
#     max_v = max(result.items(), key = lambda n: n[1])
#     print([max_v[1], max_v[0]])
#     return [max_v[1], max_v[0]]
# class UnioFind():
#     def __init__(self, data, size):
#         # self.map = [[i + j * size + 6 for i in range(size)] for j in range(size)]
#         self.map = [[(0,(-1,-1),0) for i in range(size)] for j in range(size)]
#         self.size = size
#         self.table = data
#         self.index = 1
#
#     def find(self, coor):  # 返回二维坐标coor的值
#         # print(self.table[coor[0]][coor[1]])
#         return self.table[coor[0]][coor[1]]
#
#     def union(self, a, b):  # a,b 是坐标
#         a1 = self.find(a)
#         b1 = self.find(b)
#         if a1 == b1:
#             self.map[b[0]][b[1]] = (a1, (a[0] + 1,a[1]+1), self.find(a))
#
#         # else:
#         #     self.map[b[0]][b[1]] = (b1, b, self.find(b))
#         for x in range(self.size):
#             print(self.map[x])
#         print()


# data = UnioFind([
#     [1, 2, 3, 4, 5],
#     [1, 1, 1, 2, 3],
#     [1, 1, 1, 2, 2],
#     [1, 2, 2, 2, 1],
#     [1, 1, 1, 1, 1]], 5)
# data = UnioFind([
#     [2, 1, 2, 2, 2, 4],
#     [2, 5, 2, 2, 2, 2],
#     [2, 5, 4, 2, 2, 2],
#     [2, 5, 2, 2, 4, 2],
#     [2, 4, 2, 2, 2, 2],
#     [2, 2, 4, 4, 2, 2]], 6
# )
# for i in range(6):
#     for j in range(6):
#         if j + 1 < 6:
#             data.union((i, j), (i, j + 1))
#         if i + 1 < 6:
#             data.union((i, j), (i + 1, j))
#         if j - 1 > -1:
#             data.union((i, j), (i, j - 1))
#         if i - 1 > -1:
#             data.union((i, j), (i - 1, j))


# for i in range(4):
#     data.union((4, i), (4, i + 1))
# for i in range(4):
#     data.union((i, 4), (i + 1, 4))

# def checkio(data):
#     root = {data[0][0]}
#     current = data[0][0]
#     route_map = [[i + j * len(data) + 1 for i in range(len(data))] for j in range(len(data))]
#     print(route_map)
#     for i in range(len(data)):
#         for j in range(len(data)):
#             if data[i][j] == current:
#
#



# 之前的做法 参考了一些做法。
# import itertools
#
#
# def group(data, start, visited):
#     def get(coor):
#         return data[coor[0]][coor[1]]
#
#     def in_data(coor):
#         n = len(data)
#         return 0 <= coor[0] < n and 0 <= coor[1] < n
#
#     stack = [start]
#     checked = visited + [start]
#     number = get(start)
#
#     pts = []
#     while stack:
#         pt = stack.pop()
#         pts.append(pt)
#         for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
#             new_pt = pt[0] + d[0], pt[1] + d[1]
#             if in_data(new_pt) and new_pt not in checked:
#                 checked.append(new_pt)
#                 if get(new_pt) == number:
#                     stack.append(new_pt)
#     return len(pts), number, pts
#
#
# def checkio(data):
#     def get_unvisited_pt():
#         all_pts = itertools.product(range(len(data)), repeat = 2)
#         unvisited = [p for p in all_pts if p not in visited]
#         return unvisited[0] if unvisited else None
#
#     pt = (0, 0)
#     groups = []
#     visited = []
#     while pt is not None:
#         size, number, pts = group(data, pt, visited)
#         groups.append([size, number])
#         visited += pts
#         pt = get_unvisited_pt()
#     return max(groups, key = lambda g: g[0])

# # 学习了Union-Find之后自己写的 .失败了
# class ab():
#     def __init__(self, data, size):
#         self.size = size
#         self.data = [data[i][j] for i in range(size) for j in range(size)]
#         # print(self.data)
#         self.id = [i for i in range(size * size)]  # 数组对应位置的值即为组号
#
#     def find(self, x):  # 查询节点属于的组
#         while self.id[x] != x:
#             x = self.id[x]
#         return x
#
#     def connected(self, a, b):
#         if self.data[a] == self.data[b]:
#             return True
#         return False
#
#     def union(self, a, b):
#         if self.connected(a, b):
#             s1 = self.find(a)
#             s2 = self.find(b)
#             if self.id[s1] > self.id[s2]:
#                 self.id[a] = s2
#             elif self.id[s1] == self.id[s2]:
#                 self.id[b] = s1
#                 self.id[a] = s1
#             else:
#                 self.id[b] = s1
#             for i in range(self.size):
#                 print(self.id[i * self.size:i * self.size + self.size])
#             return True
#         return False
#
#     def res(self):
#         for i in range(self.size):
#             print(self.id[i * self.size:i * self.size + self.size])
#         ls = {}
#         for u in self.id:
#             if u in ls:
#                 ls[u] += 1
#             else:
#                 ls[u] = 1
#         a = max(ls.items(), key = lambda n: n[1])
#         print(a)
#         res = []
#         b = False
#         for i in range(self.size):
#             for j in range(self.size):
#                 if self.id[i * self.size + j] == a[0]:
#                     res.append(a[1])
#                     res.append(self.data[i * self.size + j])
#                     b = True
#                 if b: break
#             if b: break
#         print(res)
#         return res
#
#
# def checkio(data):
#     size = len(data)
#     cl = ab(data, len(data))
#     direct = ((-size, 0), (0, -1), (size, 0), (0, 1))  # 上 左 下 右
#     for i in range(0, size * size, size):  # 竖
#         for j in range(size):  # 横
#             for item in direct:  # x竖 y横
#                 x = i + item[0]
#                 y = j + item[1]
#                 dis = i + j
#                 dis2 = x + y
#                 if 0 <= x < size * size and 0 <= y < size:
#                     # print(dis, item)
#                     cl.union(dis, dis2)
#     return cl.res()
#
#
# checkio([[4, 2, 5, 5, 1, 4], [4, 4, 5, 3, 4, 1], [2, 5, 4, 1, 5, 4], [1, 3, 1, 2, 2, 4], [5, 3, 4, 2, 5, 2],
#          [4, 5, 5, 5, 5, 2]])
# checkio([
#     [1, 2, 3, 4, 5],
#     [1, 1, 1, 2, 3],
#     [1, 1, 1, 2, 2],
#     [1, 2, 2, 2, 1],
#     [1, 1, 1, 1, 1]])
# checkio([
#     [2, 1, 2, 2, 2, 4],
#     [2, 5, 2, 2, 2, 2],
#     [2, 5, 4, 2, 2, 2],
#     [2, 5, 2, 2, 4, 2],
#     [2, 4, 2, 2, 2, 2],
#     [2, 2, 4, 4, 2, 2]])
# checkio([
#     [2, 1, 2, 2, 2, 4],
#     [2, 5, 3, 2, 2, 2],
#     [2, 5, 2, 1, 1, 2],
#     [2, 5, 2, 2, 2, 2],
#     [2, 4, 1, 1, 1, 2],
#     [2, 2, 4, 4, 2, 2]])
