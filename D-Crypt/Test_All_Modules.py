"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Test_All_Modules.py
"""

import cipher_test

__mydoc__ = """
----------------------------------------------------------------------------
Test_All_Modules.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

def print_test_results(result_dict):
    for mode in result_dict:
        print(mode + ': ' + result_dict[mode])
    print()

if __name__ == '__main__':
    print(__mydoc__)

    AES_results = cipher_test.AES_Test.test_main()
    monoalphabet_cipher_results = cipher_test.Monoalphabet_Cipher_Test.test_main()
    rail_fence_technique_results = cipher_test.Rail_Fence_Technique_Test.test_main()
    shift_cipher_result = cipher_test.Shift_Cipher_Test.test_main()
    columnar_transposition_results = cipher_test.Simple_Columnar_Transposition_Test.test_main()
    vernam_cipher_result = cipher_test.Vernam_Cipher_Test.test_main()
    diffie_hellman_results = cipher_test.Diffie_Hellman_Key_Exchange_Test.test_main()

    print('------ Summary of Cipher Module Tests Results ------')
    print_test_results(AES_results)
    print_test_results(monoalphabet_cipher_results)
    print_test_results(rail_fence_technique_results)
    print_test_results(shift_cipher_result)
    print_test_results(columnar_transposition_results)
    print_test_results(vernam_cipher_result)
    print_test_results(diffie_hellman_results)