import re
# sum = 0
# handle = open('regex_sum_202169.txt')
# for line in handle:
#     found = re.findall(r'\d+',line)
#     if found:
#         for i in found:
#             sum = sum + int(i)
# print(sum)
print(sum([int(i) for i in re.findall(r'\d+', open('regex_sum_202169.txt').read())]))