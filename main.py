"""
File: main.py
Project: Feistel Cipher
File Created: Friday, 3rd November 2023 10:19:15 PM
Author: Frances Antwi-Donkor
Email: tassie515@gmail.com
Version: 1.0
Brief: Feistel Cipher to decrypt and encrypt binary bits
-----
Last Modified: Sunday, 5th November 2023 8:27:34 PM
Modified By: Frances Antwi-Donkor
-----
Copyright ©2023 Frances Antwi-Donkor
"""

import utils.logic_gate as logic


def encrypt(plaintext: str, bit_op: str, key: str) -> str:
    """The `encrypt` function takes a plaintext string, a bit operation, and a
    key as input, and returns an encrypted string by splitting the plaintext
    into two halves, encoding the right half using the bit operation and key,
    and then performing an XOR operation between the encoded right half and
    the left half.

    Parameters
    ----------
    plaintext : str
        The `plaintext` parameter is a string that represents the text that you
        want to encrypt.
    bit_op : str
        The `bit_op` parameter is a string that represents the type of bitwise
        operation to be performed. It could be one of the following values:
        "AND", "OR", "XOR", "NOT".
    key : str
        The "key" parameter is a string that represents the encryption key
        used in the encryption process.

    Returns
    -------
        a string that consists of the original right half of the plaintext
        concatenated with the encrypted version of the left half of the
        plaintext.

    """
    right_one = ""
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        length = len(plaintext) // 2
        left = plaintext[: int(length)]
        right = plaintext[int(length) :]

        encrypter = encoder(bit_op, key, right)
        right_one = logic.xor_op(encrypter, left)
    return f"{right}{right_one}"


def decrypt(cipher_text: str, bit_op: str, key: str) -> str:
    """The function `decrypt` takes a cipher text, a bit operation, and a key as input, and returns the
    decrypted text by performing the specified bit operation on the right half of the cipher text and
    the result of encoding the left half of the cipher text using the key.

    Parameters
    ----------
    cipher_text : str
        The `cipher_text` parameter is a string representing the encrypted
        text that needs to be decrypted.
    bit_op : str
        The `bit_op` parameter is a string that represents the bitwise
        operation to be performed during decryption. It could be one of the
        following values: "AND", "OR", "XOR", "NOT".
    key : str
        The "key" parameter is a string that represents the encryption key
        used to decrypt the cipher text.

    Returns
    -------
        a string that concatenates the variable `left` and `left_one`.

    """

    if len(cipher_text) % 2 != 0:
        print("Cipher text should be even")
    else:
        length = len(cipher_text) // 2
        left_one = cipher_text[: int(length)]
        right_one = cipher_text[int(length) :]

        decrypter = encoder(bit_op, key, left_one)
        left = logic.xor_op(right_one, decrypter)
    return f"{left}{left_one}"


def encoder(bit_op: str, key: str, right: str) -> str:
    """The function `encoder` takes in three parameters, `bit_op`, `key`, and
    `right`, and returns the
    result of performing a logical operation (`AND`, `OR`, or `XOR`) on the
    `key` and `right` values.

    Parameters
    ----------
    bit_op : str
        A string representing the bitwise operation to be performed. It can be
        one of the following: "AND",
    "OR", or "XOR".
    key : str
        The `key` parameter is a string that represents a binary number.
    right : str
        The `right` parameter is a string representing the right operand in
        the bitwise operation.

    Returns
    -------
        the result of the specified bitwise operation (AND, OR, or XOR)
        performed on the "key" and "right" strings.

    """
    if bit_op == "AND":
        return logic.and_op(key, right)
    elif bit_op == "OR":
        return logic.or_op(key, right)
    elif bit_op == "XOR":
        return logic.xor_op(key, right)
