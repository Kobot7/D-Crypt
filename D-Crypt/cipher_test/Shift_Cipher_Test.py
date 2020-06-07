"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Shift_Cipher_Test.py
"""

from cipher import Shift_Cipher

__mydoc__ = """
----------------------------------------------------------------------------
Shift_Cipher_Test.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def run_test(key, plaintext, encryptionString):
    print("Plaintext: " + plaintext)
    ciphertext = Shift_Cipher.encrypt(key, plaintext, encryptionString)
    print("Ciphertext: " + ciphertext)
    decryptedtext = Shift_Cipher.decrypt(key, ciphertext, encryptionString)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def test_main():
    key = 3
    plaintext = 'Hello World! I hope this cipher module is working.'

    print('---------- Shift Cipher test ----------')
    Shift_Cipher_dict = {'Shift Cipher (only alpha)': run_test(key, plaintext, 'alpha')
        , 'Shift Cipher (base64)': run_test(key, plaintext, 'base64')
                         }

    return Shift_Cipher_dict

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)
    print(Shift_Cipher.__mydoc__)

    print_test_results(test_main())