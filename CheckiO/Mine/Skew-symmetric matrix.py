"""
File name: Skew-symmetric matrix
Reference: https://checkio.org/mission/skew-symmetric-matrix/
Time: 2016-05-07
By: enihsyou
"""


def checkio(matrix):
    return all([[matrix[j][i] for j in range(len(matrix))] == list(map(lambda x: -x, matrix[i])) for i in
                range(len(matrix))])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
