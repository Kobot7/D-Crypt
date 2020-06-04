"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D' Crypt
Vernam_Cipher_Test.py
"""

from cipher import Vernam_Cipher

__mydoc__ = """
----------------------------------------------------------------------------
Vernam_Cipher_Test.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def run_test(plaintext, key):
    print("Plaintext: " + plaintext)
    ciphertext = Vernam_Cipher.encrypt(plaintext, key)
    print("Ciphertext: " + ciphertext)
    decryptedtext = Vernam_Cipher.decrypt(ciphertext, key)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def test_main():
    key = 'LWYCKIQTAQANZSCMFNVHVVLOHVUZRRPKRVVCQRXF'
    plaintext = 'HELLOWORLDIHOPETHISCIPHERMODULEISWORKING'

    print('---------- Vernam Cipher test ----------')
    Vernam_Cipher_dict = {'Vernam Cipher': run_test(plaintext, key)}

    return Vernam_Cipher_dict

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)
    print(Vernam_Cipher.__mydoc__)

    print_test_results(test_main())