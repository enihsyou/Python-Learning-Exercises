###Solve 1

# from fractions import Fraction
# from numpy import matrix
#
#
# def fractionalize(data):
#     return Fraction(round(data) / 100)
#
#
# def checkio(data):
#     matr = [[0 for i in range(4)] for j in range(3)]
#     matr2 = [[Fraction(b)] for b in data.values()]
#     proportion = {
#         'gold': 0,
#         'iron': 1,
#         'tin': 2,
#         'copper': 3}
#     for index, item in enumerate(data.keys()):
#         sep = item.split('-')
#         for it in sep:
#             matr[index][proportion[it]] = 1
#     Ig = matrix(matr).I.dot(100)
#     print(Ig)
#     vfunc = np.vectorize(fractionalize)
#     c = vfunc(Ig)
#     print(c)
#     res = c.dot(matrix(matr2)).dot(2)
#     print(Ig)
#     print(res)
#     print(res.tolist()[0][0])
#     return res.tolist()[0][0]

###Solve 2
from fractions import Fraction


# def checkio(data):
#     gold = Fraction(0)
#     iron = Fraction(0)
#     copper = Fraction(0)
#     tin = Fraction(0)
#     whole = Fraction(0)
#     proportion = {
#         'gold': 0,
#         'iron': 0,
#         'tin': 0,
#         'copper': 0}
#     for index, item in enumerate(data.keys()):
#         sep = item.split('-')
#         for i in sep:
#             proportion[i] += 1
#         whole += data[item]
#     a = proportion[max(proportion, key = lambda x: proportion[x])]
#     b = proportion[min(proportion, key = lambda x: proportion[x])]
#     a -= b
#     whole -= b
#     print(whole / a)
#     if proportion['gold'] == 3:
#         print(whole / a)
#         return whole / a
#     if proportion['gold'] == 0:
#         print(1 - whole / a)
#         return 1 - whole / a
#     for i in range(3):
#         if list(proportion.values()).count(i) == 3:
#             it = 0
#             for item in proportion.keys():
#                 if proportion[item] != i:
#                     it = item
#                     break
#             it =
#     return
def checkio(alloys):
    return 1 - sum([1 - v if 'gold' in k else v for (k, v) in alloys.items()]) / 2


checkio({
    'tin-copper' : Fraction(5, 9),
    'gold-tin'   : Fraction(1, 2),
    'copper-gold': Fraction(2, 7),
})

checkio({
    'tin-iron'   : Fraction(2, 3),
    'gold-iron'  : Fraction(1, 2),
    'copper-iron': Fraction(1, 4),
})

checkio({
    'tin-iron'   : Fraction(1, 2),
    'iron-copper': Fraction(1, 2),
    'copper-tin' : Fraction(1, 2),
})

checkio({
    'gold-tin'   : Fraction(1, 2),
    'gold-iron'  : Fraction(1, 3),
    'gold-copper': Fraction(1, 4),
})
