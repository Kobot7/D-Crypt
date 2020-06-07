"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Vernam_Cipher.py
"""

__mydoc__ = """
----------------------------------------------------------------------------
Vernam_Cipher.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

values = {
    'A': 0, 0: 'A'
    , 'B': 1, 1: 'B'
    , 'C': 2, 2: 'C'
    , 'D': 3, 3: 'D'
    , 'E': 4, 4: 'E'
    , 'F': 5, 5: 'F'
    , 'G': 6, 6: 'G'
    , 'H': 7, 7: 'H'
    , 'I': 8, 8: 'I'
    , 'J': 9, 9: 'J'
    , 'K': 10, 10: 'K'
    , 'L': 11, 11: 'L'
    , 'M': 12, 12: 'M'
    , 'N': 13, 13: 'N'
    , 'O': 14, 14: 'O'
    , 'P': 15, 15: 'P'
    , 'Q': 16, 16: 'Q'
    , 'R': 17, 17: 'R'
    , 'S': 18, 18: 'S'
    , 'T': 19, 19: 'T'
    , 'U': 20, 20: 'U'
    , 'V': 21, 21: 'V'
    , 'W': 22, 22: 'W'
    , 'X': 23, 23: 'X'
    , 'Y': 24, 24: 'Y'
    , 'Z': 25, 25: 'Z'
}

def encrypt(plaintext, key):
    plaintext = plaintext.replace(' ', '').upper()
    key = key.replace(' ', '').upper()
    ciphertext = ''

    for index in range(len(plaintext)):
        ciphertext += values[(values[plaintext[index]] + values[key[index]]) % 26]

    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(' ', '').upper()
    key = key.replace(' ', '').upper()
    plaintext = ''

    for index in range(len(ciphertext)):
        letterValue = (values[ciphertext[index]] - values[key[index]])

        if letterValue < 0:
            letterValue += 26

        plaintext += values[letterValue]

    return plaintext