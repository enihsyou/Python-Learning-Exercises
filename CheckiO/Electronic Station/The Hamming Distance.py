def checkio(pos1, pos2):
    return str(bin(pos1 ^ pos2))[2:].count('1')


checkio(1, 2)
