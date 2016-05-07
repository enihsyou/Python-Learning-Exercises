"""
File name: Flatten a list
Reference: https://checkio.org/mission/flatten-list/
Time: 2016-05-07
By: enihsyou
"""

flat_list = lambda x: eval('[' + str(x).replace('[', '').replace(']', '') + ']')
# flat_list = lambda L: sum(map(flat_list, L), []) if isinstance(L, list) else [L]  # 别人的做法
print(flat_list([1, [2, 2, 2], 4]))
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
