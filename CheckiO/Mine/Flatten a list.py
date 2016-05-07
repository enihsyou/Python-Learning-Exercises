"""
File name: Flatten a list
Reference: https://checkio.org/mission/flatten-list/
Time: 2016-05-07
By: enihsyou
"""

# c = lambda x: x
# flat_list = lambda x: [a if isinstance(a, int) else c(a) for a in x]
flat_list = lambda x: eval('[' + str(x).replace('[', '').replace(']', '') + ']')
print(flat_list([1, [2, 2, 2], 4]))
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
