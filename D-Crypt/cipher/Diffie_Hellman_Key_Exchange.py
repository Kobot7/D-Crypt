"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Diffie_Hellman_Key_Exchange.py
"""

__mydoc__ = """
----------------------------------------------------------------------------
Diffie_Hellman_Key_Exchange.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def calculate(n, g, A, B):
    n = int(n)
    g = int(g)
    A = int(A)
    B = int(B)

    aNo = (g**A) % n
    bNo = (g**B) % n

    aKey = (bNo**A) % n
    bKey = (aNo**B) % n

    if aKey==bKey:
        return aKey

    else:
        return None