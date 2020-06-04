"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D' Crypt
Rail_Fence_Technique.py
"""

__mydoc__ = """
----------------------------------------------------------------------------
Rail_Fence_Technique.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def encrypt(plaintext, key, encryptionString):
    if encryptionString == 'no-space':
        plaintext = plaintext.replace(' ', '')

    rail = []
    for x in range(key): # create empty rail
        newRailRow = []
        for y in range(len(plaintext)):
            newRailRow.append('')
        rail.append(newRailRow)

    dir_down = False
    row = 0
    col = 0

    for i in range(len(plaintext)):
        # change direction if reach top or bottom of rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # append the letter to the matrix
        rail[row][col] = plaintext[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    ciphertext = ''
    for x in range(key):
        for y in range(len(plaintext)):
            if rail[x][y] != '':
                ciphertext += rail[x][y]

    return ciphertext


def decrypt(ciphertext, key, encryptionString):
    if encryptionString == 'no-space':
        ciphertext = ciphertext.replace(' ', '')

    rail = []
    for x in range(key):  # create empty rail
        newRailRow = []
        for y in range(len(ciphertext)):
            newRailRow.append('')
        rail.append(newRailRow)

    dir_down = False
    row = 0
    col = 0

    # mark the rail tracks with '*'
    for x in range(len(ciphertext)):
        # change direction if reach top or bottom of rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    # fill in rail tracks with ciphertext
    index = 0
    for x in range(key):
        for y in range(len(ciphertext)):
            if rail[x][y] == '*' and index < len(ciphertext):
                rail[x][y] = ciphertext[index]
                index += 1

    dir_down = False
    plaintext = ''
    row = 0
    col = 0
    for x in range(len(ciphertext)):
        # change direction if reach top or bottom of rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        if (rail[row][col] != ''):
            plaintext += rail[row][col]
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return plaintext