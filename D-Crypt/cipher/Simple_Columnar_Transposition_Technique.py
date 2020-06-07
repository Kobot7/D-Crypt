"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Simple_Columnar_Transposition_Technique.py
"""

__mydoc__ = """
----------------------------------------------------------------------------
Simple_Columnar_Transposition_Technique.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

import math
def encrypt(plaintext, key, encryptionString):
    if encryptionString == 'no-space':
        plaintext = plaintext.replace(' ', '')

    ciphertext = ''

    # track key indices
    key_index = 0
    key_order = sorted(list(key))

    msg_len = len(plaintext)
    msg_list = list(plaintext)

    # calculate no. of column of the matrix
    col = len(key)

    # calculate no. of rows needed for the matrix
    row = int(math.ceil(msg_len / col))

    # add 'null' to fill remaining empty cell of the matrix
    fill_null = int((row * col) - msg_len)
    for x in range(fill_null):
        msg_list.append(None)

    # create matrix and insert plaintext in rows
    matrix = []

    for i in range(0, len(msg_list)-1, col):
        matrix.append(msg_list[i: i + col])

    # read matrix column-wise in order of the key
    for x in range(col):
        # get current column
        curr_idx = key.index(key_order[key_index])

        for row in matrix:
            if row[curr_idx] != None:
                ciphertext += row[curr_idx]

        key_index += 1

    return ciphertext

def decrypt(ciphertext, key, encryptionString):
    if encryptionString == 'no-space':
        ciphertext = ciphertext.replace(' ', '')

    plaintext = ""

    # track key indices
    key_index = 0
    key_order = sorted(list(key))

    # track msg indices
    msg_index = 0
    msg_len = len(ciphertext)
    msg_list = list(ciphertext)

    # calculate no. of column of the matrix
    col = len(key)

    # calculate no. of rows needed for the matrix
    row = int(math.ceil(msg_len / col))

    # add 'null' to fill remaining empty cell of the matrix
    fill_null = int((row * col) - msg_len)
    if fill_null != 0:
        for x in range(fill_null+1):
            msg_list.insert((3-x)*row - 1, None)

    # create an empty matrix
    matrix = []
    for x in range(row):
        matrix += [[None] * col]

    # arrange ciphertext by columns in order of key
    for x in range(col):
        curr_idx = key.index(key_order[key_index])

        for y in range(row):
            matrix[y][curr_idx] = msg_list[msg_index]
            msg_index += 1
        key_index += 1

    # convert matrix into a string
    for row in matrix:
        for letter in row:
            if letter!=None:
                plaintext += letter

    return plaintext