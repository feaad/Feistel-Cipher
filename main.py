'''
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
'''

import utils.logic_gate as logic


def encrypt(plaintext: str, bit_op: str, key: str):
    cipher_text = ''
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        left = plaintext[:int(len(plaintext)/2)]
        right = plaintext[int(len(plaintext)/2):]
        
        end = encoder(bit_op, key, right)
        cipher_text = xor_left('1001', '1110')
    
    print(cipher_text)
   
        
def encoder(bit_op: str, key: str, right: str):
    if bit_op == 'AND':
        encode = logic.and_op(key, right) 
        return encode
    elif bit_op == 'OR':
        encode = logic.or_op(key, right) 
        return encode
    elif bit_op == 'XOR':
        encode = logic.xor_op(key, right) 
        return encode
    
    
def xor_left(left: str, encode: str):
    return logic.xor_op(encode, left)
    


encrypt("10010011", "AND", "1101")
# xor_left('1001', '1110')
