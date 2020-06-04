"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D' Crypt
Shift_Cipher.py
"""

__mydoc__ = """
----------------------------------------------------------------------------
Shift_Cipher.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""


def encrypt(key, plaintext, encryptionString):
    ciphertext = ''

    if encryptionString == 'alpha':
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    else:
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    for character in plaintext:
        if character in LETTERS:
            # get the character position
            position = LETTERS.find(character)
            position = position + key

            # wrap-around if position >= length of LETTERS
            if position >= len(LETTERS):
                position = position - len(LETTERS)

            # append encrypted character
            ciphertext = ciphertext + LETTERS[position]

        else:
            # append character without encrypting
            ciphertext = ciphertext + character

    return ciphertext


def decrypt(key, ciphertext, encryptionString):
    decryptedtext = ""

    if encryptionString=='alpha':
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    else:
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    for character in ciphertext:
        if character in LETTERS:
            # get the character position
            position = LETTERS.find(character)
            position = position - key

            # wrap-around if position >= length of LETTERS
            if position < 0:
                position = position + len(LETTERS)

            # append encrypted character
            decryptedtext = decryptedtext + LETTERS[position]

        else:
            # append character without encrypting
            decryptedtext = decryptedtext + character

    return decryptedtext