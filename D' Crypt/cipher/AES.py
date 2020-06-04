"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D' Crypt
AES.py
"""

__mydoc__ = """
----------------------------------------------------------------------------
AES.py, Ko Jia Ling
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


def encrypt_ECB(plaintext, key):
    plaintext = bytes(plaintext, 'utf-8')
    key = bytes(key, 'utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    ciphertext = b64encode(ciphertext_bytes).decode('utf-8')
    return ciphertext

def decrypt_ECB(ciphertext, key):
    ciphertext = b64decode(ciphertext.encode('utf-8'))
    key = bytes(key, 'utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext



def encrypt_CBC(plaintext, key, iv):
    plaintext = bytes(plaintext, 'utf-8')
    key = bytes(key, 'utf-8')
    iv = bytes(iv, 'utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    ciphertext = b64encode(ciphertext_bytes).decode('utf-8')
    return ciphertext

def decrypt_CBC(ciphertext, key, iv):
    ciphertext = b64decode(ciphertext.encode('utf-8'))
    key = bytes(key, 'utf-8')
    iv = bytes(iv, 'utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext



def encrypt_CFB(plaintext, key, iv):
    plaintext = bytes(plaintext, 'utf-8')
    key = bytes(key, 'utf-8')
    iv = bytes(iv, 'utf-8')
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ciphertext_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    ciphertext = b64encode(ciphertext_bytes).decode('utf-8')
    return ciphertext

def decrypt_CFB(ciphertext, key, iv):
    ciphertext = b64decode(ciphertext.encode('utf-8'))
    key = bytes(key, 'utf-8')
    iv = bytes(iv, 'utf-8')
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    plaintext_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext


def encrypt_OFB(plaintext, key, iv):
    plaintext = bytes(plaintext, 'utf-8')
    key = bytes(key, 'utf-8')
    iv = bytes(iv, 'utf-8')
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    ciphertext_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    ciphertext = b64encode(ciphertext_bytes).decode('utf-8')
    return ciphertext

def decrypt_OFB(ciphertext, key, iv):
    ciphertext = b64decode(ciphertext.encode('utf-8'))
    key = bytes(key, 'utf-8')
    iv = bytes(iv, 'utf-8')
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    plaintext_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext