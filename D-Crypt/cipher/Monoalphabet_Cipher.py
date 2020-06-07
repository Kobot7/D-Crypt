"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Monoalphabet_Cipher.py
"""

__mydoc__ = """
----------------------------------------------------------------------------
Monoalphabet_Cipher.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        if letter in letters.upper():
            index = letters.find(letter)
            ciphertext += key[index].upper()

        elif letter in letters.lower():
            index = letters.lower().find(letter)
            ciphertext += key[index].lower()

        else:
            ciphertext += letter

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        if letter in letters.upper():
            index = key.upper().find(letter)
            plaintext += letters[index].upper()

        elif letter in letters.lower():
            index = key.lower().find(letter)
            plaintext += letters[index].lower()

        else:
            plaintext += letter

    return plaintext