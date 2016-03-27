import re


def decode_vigenere(old_message, old_encrypted, new_message):
    # 旧的文本和旧的加密文本之间的距离
    distance = [(ord(old_encrypted[i]) - ord(old_message[i])) % 26
                for i in range(len(old_encrypted))]
    # 计算出Key
    key = "".join(map(lambda x, y: chr((ord(x) - ord(y)) % 26 + 65), old_encrypted, old_message))
    print(list(map(lambda x, y: chr((ord(x) - ord(y)) % 26 + 65), old_encrypted, old_message)))

    key_start = re.findall(r"(.+?)\1.+", key)
    if key_start and key.startswith(key_start[0]):
        for i in range(len(key)):
            if key_start[0][i % len(key_start[0])] != key[i % len(key_start[0])]:
                break
            elif i == len(key):
                key = key_start[0]

    key_message = ((len(new_message) // len(key) + 1) * key)[:len(new_message)]
    new = [chr((ord(new_message[i]) - ord(key_message[i])) % 26 + 65)
           for i in range(len(new_message))]
    result = "".join(new)
    return result


decode_vigenere(u"AAAAAAAAA", u"ABABABABC", u"ABABABABC")
decode_vigenere('LOREMIPSUM',
                'OCCSDQJEXA',
                'OCCSDQJEXA')
decode_vigenere('HELLO', 'OIWWC', 'ICP')
decode_vigenere('DONTWORRYBEHAPPY',
                'FVRVGWFTFFGRIDRF',
                'DLLCZXMFVRVGWFTF')
decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT",
                u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI",
                u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL")
