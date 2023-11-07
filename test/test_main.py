"""
File: test_main.py
Project: Feistel Cipher
File Created: Sunday, 5th November 2023 7:48:24 PM
Author: Frances Antwi-Donkor
Email: tassie515@gmail.com
Version: 1.0
Brief: 
-----
Last Modified: Sunday, 5th November 2023 8:23:36 PM
Modified By: Frances Antwi-Donkor
-----
Copyright ©2023 Frances Antwi-Donkor
"""

import pytest
import main


# @pytest.mark.skip(reason="Incomplete")
def test_encoder():
    """
    The function `test_encoder()` tests the `encrypt()` function by passing
    in a binary string, an operation, and a key(binary string), and asserts
    that the result is equal to a given expected output.

    """
    result = main.encrypt("10010011", "OR", "1101")
    assert result == "00110110"


def test_decryter():
    """
    The function `test_decryter()` tests the `decrypt()` function by passing
    in a binary string, an operation, and a key(binary string), and asserts
    that the result is equal to a given expected output.

    """

    result = main.decrypt("10010011", "OR", "1101")
    assert result == "11101001"
