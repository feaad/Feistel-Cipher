"""
File: main.py
Project: Feistel Cipher
File Created: Friday, 3rd November 2023 10:19:15 PM
Author: Frances Antwi-Donkor
Email: tassie515@gmail.com
Version: 1.0
Brief: 
-----
Last Modified: Sunday, 5th November 2023 8:27:34 PM
Modified By: Frances Antwi-Donkor
-----
Copyright ©2023 Frances Antwi-Donkor
"""

import utils.logic_gate as logic


def encrypt(plaintext: str, bit_op: str, key: str):   
    '''Encrypt takes in 3 parameters to encrypt binary code'''
    right_one = ""
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        left = plaintext[: int(len(plaintext) // 2)]
        right = plaintext[int(len(plaintext) // 2):]

        end = encoder(bit_op, key, right)
        right_one = xor_left(end, left)
    return f"{right}{right_one}"


def encoder(bit_op: str, key: str, right: str):
    '''Creates an encoder with respect to the logic gates'''
    if bit_op == "AND":
        return logic.and_op(key, right)
    elif bit_op == "OR":
        return logic.or_op(key, right)
    elif bit_op == "XOR":
        return logic.xor_op(key, right)


def xor_left(left: str, encode: str):
    '''An xor function to obtain the right_one binary code'''
    return logic.xor_op(encode, left)


encrypt("10010011", "AND", "1101")
