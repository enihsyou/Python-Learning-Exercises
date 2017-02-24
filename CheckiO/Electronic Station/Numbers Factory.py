# former thinking


# ways to get prime list in range(10)
# def prime():
#     for num in range(10):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 yield num
#
#
# factor giving data
# def factor(data):
#     return [i for i in range(1, data + 1) if data % i == 0]
#
#
# def factor_dict(data):
#     dict = {}
#     for item in data:
#         dict[item] = factor(item)
#     return dict
#
#
# def fact_list(data, dict):
#     result = []
#     for i in range(len(data)):
#         for j in range(i, len(data)):
#             if data[i] * data[j] == data[-1]:
#                 result.append([data[i], data[j]])
#     return result
#
#
# def checkio(input):
#     input_factor_number = factor(input)
#     input_factor_number_dict = factor_dict(input_factor_number)
#     fact = fact_list(input_factor_number, input_factor_number_dict)
#     if fact:
#         for i in range(len(fact)):
#             lst = []
#             for j in range(len(fact[0])):
#                 lst.append(input_factor_number_dict[fact[i][j]])
#             print(lst)

# my answer:
def checkio(data):
    number = data
    fact = []
    for i in "98765432":
        while number % int(i) == 0:
            number //= int(i)
            fact.append(i)
    if number >= 10: return 0
    result = int(''.join(sorted(fact))) if len(fact) > 1 else 0
    return result


checkio(3275)
