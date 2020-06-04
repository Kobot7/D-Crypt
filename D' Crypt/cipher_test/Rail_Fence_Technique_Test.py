"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D' Crypt
Rail_Fence_Technique_Test.py
"""

from cipher import Rail_Fence_Technique

__mydoc__ = """
----------------------------------------------------------------------------
Rail_Fence_Technique_Test.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def run_test(plaintext, key, encryptionString):
    print("Plaintext: " + plaintext)
    ciphertext = Rail_Fence_Technique.encrypt(plaintext, key, encryptionString)
    print("Ciphertext: " + ciphertext)
    decryptedtext = Rail_Fence_Technique.decrypt(ciphertext, key, encryptionString)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def test_main():
    key = 3
    plaintext = 'Hello World! I hope this cipher module is working.'

    print('---------- Rail Fence Technique test ----------')
    RFT_dict = {'Rail Fence Technique (with space)': run_test(plaintext, key, "space")
                , 'Rail Fence Technique (no space)':  run_test(plaintext.replace(' ', ''), key, "no-space")
                }

    return RFT_dict

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)
    print(Rail_Fence_Technique.__mydoc__)

    print_test_results(test_main())