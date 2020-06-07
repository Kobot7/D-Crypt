"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Diffie_Hellman_Key_Exchange_Test.py
"""

from cipher import Diffie_Hellman_Key_Exchange

__mydoc__ = """
----------------------------------------------------------------------------
Diffie_Hellman_Key_Exchange_Test.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def run_test(n, g, A, B):
    print("n: " + n)
    print("g: " + g)
    print("A: " + A)
    print("B: " + B)

    key = Diffie_Hellman_Key_Exchange.calculate(n, g, A, B)
    print('Key: ' + str(key))
    print("\n")

    if key==3:
        return 'Yes'
    else:
        return 'No'

def test_main():
    n = '23'
    g = '59'
    A = '82'
    B = '70'
    print('---------- Diffie Hellman Key Exchange test ----------')
    Monoalphabet_Cipher_dict = {'Diffie Hellman Key Exchange': run_test(n, g, A, B)}

    return Monoalphabet_Cipher_dict

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)
    print(Diffie_Hellman_Key_Exchange.__mydoc__)

    print_test_results(test_main())