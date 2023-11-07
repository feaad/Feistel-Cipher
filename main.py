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


def encrypt(plaintext: str, bit_op: str, key: str) -> str:
    """The function encrypt() takes in a key and a logic operand to encrypt
    binary code"""

    right_one = ""
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        left = plaintext[: int(len(plaintext) // 2)]
        right = plaintext[int(len(plaintext) // 2) :]

        encrypter = encoder(bit_op, key, right)
        right_one = xor(encrypter, left)
    return f"{right}{right_one}"


def decrypt(cipher_text: str, bit_op: str, key: str) -> str:
    """The function decrypt() takes in a key and a logic operand to decrypt
    binary code"""
    if len(cipher_text) % 2 != 0:
        print("Ciphertext should be even")
    else:
        left_one = cipher_text[: int(len(cipher_text) // 2)]
        right_one = cipher_text[int(len(cipher_text) // 2) :]

        decrypter = encoder(bit_op, key, left_one)
        left = xor(right_one, decrypter)
    return f"{left}{left_one}"


def encoder(bit_op: str, key: str, right: str) -> str:
    """Creates an encoder with respect to the logic gates"""
    if bit_op == "AND":
        return logic.and_op(key, right)
    elif bit_op == "OR":
        return logic.or_op(key, right)
    elif bit_op == "XOR":
        return logic.xor_op(key, right)


def xor(binary_bit: str, encode: str) -> str:
    """An xor function to obtain the right_one binary code"""
    return logic.xor_op(encode, binary_bit)
