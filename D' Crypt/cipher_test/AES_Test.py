"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D' Crypt
AES_Test.py
"""

from cipher import AES

__mydoc__ = """
----------------------------------------------------------------------------
AES_Test.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def run_test_ECB(plaintext, key):
    print("Plaintext: " + plaintext)
    ciphertext = AES.encrypt_ECB(plaintext, key)
    print("Ciphertext: " + ciphertext)
    decryptedtext = AES.decrypt_ECB(ciphertext, key)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def run_test_CBC(plaintext, key, iv):
    print("Plaintext: " + plaintext)
    ciphertext = AES.encrypt_CBC(plaintext, key, iv)
    print("Ciphertext: " + ciphertext)
    decryptedtext = AES.decrypt_CBC(ciphertext, key, iv)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def run_test_CFB(plaintext, key, iv):
    print("Plaintext: " + plaintext)
    ciphertext = AES.encrypt_CFB(plaintext, key, iv)
    print("Ciphertext: " + ciphertext)
    decryptedtext = AES.decrypt_CFB(ciphertext, key, iv)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def run_test_OFB(plaintext, key, iv):
    print("Plaintext: " + plaintext)
    ciphertext = AES.encrypt_OFB(plaintext, key, iv)
    print("Ciphertext: " + ciphertext)
    decryptedtext = AES.decrypt_OFB(ciphertext, key, iv)
    print("Decrypted text: " + decryptedtext)
    print("\n")

    if plaintext==decryptedtext:
        return 'Yes'
    else:
        return 'No'

def test_main():
    key_128 = 'testing128bitkey'
    key_192 = 'testingUsing192BitKey!:)'
    key_256 = 'testing256bitkeyidkwhattotypenow'
    iv = 'testivhahahahaha'
    plaintext = 'Hello World! I hope this cipher module is working.'

    print('---------- AES ECB Cipher test ----------')
    AES_dict = {'AES ECB (128-bit key)': run_test_ECB(plaintext, key_128)
                , 'AES ECB (192-bit key)': run_test_ECB(plaintext, key_192)
                , 'AES ECB (256-bit key)': run_test_ECB(plaintext, key_256)
                }

    print('---------- AES CBC Cipher test ----------')
    AES_dict['AES CBC (128-bit key)'] = run_test_CBC(plaintext, key_128, iv)
    AES_dict['AES CBC (192-bit key)'] = run_test_CBC(plaintext, key_192, iv)
    AES_dict['AES CBC (256-bit key)'] = run_test_CBC(plaintext, key_256, iv)

    print('---------- AES CFB Cipher test ----------')
    AES_dict['AES CBC (128-bit key)'] = run_test_CFB(plaintext, key_128, iv)
    AES_dict['AES CBC (192-bit key)'] = run_test_CFB(plaintext, key_192, iv)
    AES_dict['AES CBC (256-bit key)'] = run_test_CFB(plaintext, key_256, iv)

    print('---------- AES OFB Cipher test ----------')
    AES_dict['AES OFB (128-bit key)'] = run_test_OFB(plaintext, key_128, iv)
    AES_dict['AES OFB (192-bit key)'] = run_test_OFB(plaintext, key_192, iv)
    AES_dict['AES OFB (256-bit key)'] = run_test_OFB(plaintext, key_256, iv)

    return AES_dict

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)
    print(AES.__mydoc__)

    print_test_results(test_main())