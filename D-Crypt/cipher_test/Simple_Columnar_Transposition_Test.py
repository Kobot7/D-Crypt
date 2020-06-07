"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Simple_Columnar_Transposition_Technique_Test.py
"""

from cipher import Simple_Columnar_Transposition_Technique

__mydoc__ = """
----------------------------------------------------------------------------
Simple_Columnar_Transposition_Technique_Test.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def run_test(plaintext, key, encryptionString):
    print("Plaintext: " + plaintext)
    ciphertext = Simple_Columnar_Transposition_Technique.encrypt(plaintext, key, encryptionString)
    print("Ciphertext: " + ciphertext)
    decryptedtext = Simple_Columnar_Transposition_Technique.decrypt(ciphertext, key, encryptionString)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def test_main():
    key = 'KAI'
    plaintext = 'Hello World! I hope this cipher module is working.'

    print('---------- Simple Columnar Transposition test ----------')
    Simple_Columnar_Transposition_dict = {
        'Simple Columnar Transposition (with space)': run_test(plaintext, key, 'space')
        , 'Simple Columnar Transposition (no space)': run_test(plaintext.replace(' ', ''), key, 'no-space')
        }

    return Simple_Columnar_Transposition_dict

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)
    print(Simple_Columnar_Transposition_Technique.__mydoc__)

    print_test_results(test_main())