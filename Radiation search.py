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
import itertools


def group(data, start, visited):
    def get(coor):
        return data[coor[0]][coor[1]]

    def in_data(coor):
        n = len(data)
        return 0 <= coor[0] < n and 0 <= coor[1] < n

    stack = [start]
    checked = visited + [start]
    number = get(start)

    pts = []
    while stack:
        pt = stack.pop()
        pts.append(pt)
        for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            new_pt = pt[0] + d[0], pt[1] + d[1]
            if in_data(new_pt) and new_pt not in checked:
                checked.append(new_pt)
                if get(new_pt) == number:
                    stack.append(new_pt)
    return len(pts), number, pts


def checkio(data):
    def get_unvisited_pt():
        all_pts = itertools.product(range(len(data)), repeat = 2)
        unvisited = [p for p in all_pts if p not in visited]
        return unvisited[0] if unvisited else None

    pt = (0, 0)
    groups = []
    visited = []
    while pt is not None:
        size, number, pts = group(data, pt, visited)
        groups.append([size, number])
        visited += pts
        pt = get_unvisited_pt()
    return max(groups, key = lambda g: g[0])


checkio([
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3],
    [1, 1, 1, 2, 2],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]])
checkio([
    [2, 1, 2, 2, 2, 4],
    [2, 5, 2, 2, 2, 2],
    [2, 5, 4, 2, 2, 2],
    [2, 5, 2, 2, 4, 2],
    [2, 4, 2, 2, 2, 2],
    [2, 2, 4, 4, 2, 2]])
checkio([
    [2, 1, 2, 2, 2, 4],
    [2, 5, 3, 2, 2, 2],
    [2, 5, 2, 1, 1, 2],
    [2, 5, 2, 2, 2, 2],
    [2, 4, 1, 1, 1, 2],
    [2, 2, 4, 4, 2, 2]])
