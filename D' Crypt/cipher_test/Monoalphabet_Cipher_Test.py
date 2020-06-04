"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D' Crypt
Monoalphabet_Cipher_Test.py
"""

from cipher import Monoalphabet_Cipher

__mydoc__ = """
----------------------------------------------------------------------------
Monoalphabet_Cipher_Test.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def run_test(plaintext, key):
    print("Plaintext: " + plaintext)
    ciphertext = Monoalphabet_Cipher.encrypt(plaintext, key)
    print("Ciphertext: " + ciphertext)
    decryptedtext = Monoalphabet_Cipher.decrypt(ciphertext, key)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def test_main():
    key = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
    plaintext = 'Hello World! I hope this cipher module is working.'

    print('---------- Mono-alphabet Cipher test ----------')
    Monoalphabet_Cipher_dict = {'Mono-alphabet Cipher': run_test(plaintext, key)}

    return Monoalphabet_Cipher_dict

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)
    print(Monoalphabet_Cipher.__mydoc__)

    print_test_results(test_main())