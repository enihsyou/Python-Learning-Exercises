# def dec2bin(input):
#     num = int(input)
#     mid = []
#     while True:
#         if num == 0: break
#         num, rem = divmod(num, 2)
#         mid.append(rem)
#
#     return ''.join([str(x) for x in mid[::-1]]).rjust(8, '0')
#
#
# def bin2dec(input):
#     return str(int(input, 2))
#
#
# def checkio(input):
#     data = []
#     subnet = 0
#     phraseddata = []
#
#     for item in input:
#         strs = ""
#         for i in item.split('.'):
#             strs += dec2bin(i)
#         data.append(strs)
#     #print(data)
#
#     lst = [[data[i][index] for i in range(len(data))] for index in range(32)]
#     #print(lst)
#
#     for index in range(len(lst)):
#         if lst[index].count(lst[index][0]) != len(data):
#             #print(index)
#             subnet = index
#             break
#
#     data = [data[i][:subnet].ljust(32, '0') for i in range(len(data))]
#     #print(data)
#
#     for item in data:
#         phraseddata = [item[:8], item[8:16], item[16:24], item[24:]]
#         strs = '.'.join(phraseddata)
#         #print(strs)
#         phraseddata = [bin2dec('0b' + phraseddata[i]) for i in range(len(phraseddata))]
#         #print(phraseddata)
#
#     result = '.'.join(phraseddata) + '/' + str(subnet)
#     #print(result)
#     return result


# def checkio(data):
#     # functions to convert string ip representation to 32bit integer and vice versa
#     str2ip = lambda ip: sum(int(n) * (256 ** p) for p, n in enumerate(reversed(ip.split('.'))))
#     ip2str = lambda ip: '.'.join(str((ip & (1 << i) - 1) >> (i - 8)) for i in range(32, 0, -8))
#
#     ips = [str2ip(i) for i in data]  # convert string ip representaion to ints
#
#     # min and max ip are enought to find out common left bits for all ips in data
#     ip1 = min(ips)  # min ip from data
#     ip2 = max(ips)  # max ip from data
#     diff = ip1 ^ ip2  # calculate bits which is different for min and max ips
#
#     # next cycle is to calculate number of significant bits in 'diff' and then
#     # 'subnet' = 32 - 'number of significant bits'
#     subnet = 32
#     mask = (1 << 32) - 1  # 0b 11111111 11111111 11111111 11111111
#     while diff:  # while diff has set bits
#         diff >>= 1  # shift all bits to right by one place
#         mask <<= 1  # shift all bits to left by one place and add 0 bit to the end
#         subnet -= 1  # decrease subnet number
#
#     network = ip1 & mask  # put mask on any of ips
#
#     return '%s/%d' % (ip2str(network), subnet)


def checkio(data):
    routes = [''.join([bin(int(x))[2:].zfill(8) for x in i.split('.')]) for i in data]
    new_route = ''
    for i in range(32):
        for j in range(len(routes) - 1):
            if routes[0][i] == routes[j + 1][i]:
                d = routes[0][i]
            else:
                new_route = new_route.ljust(32, '0')
                return (
                    str(int(new_route[:8], 2)) + '.' +
                    str(int(new_route[8:16], 2)) + '.' +
                    str(int(new_route[16:24], 2)) + '.' +
                    str(int(new_route[24:32], 2)) + '/' + str(i)
                )
        new_route += d
        d = ''



checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"])
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
#     assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
#     assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
