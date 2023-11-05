import utils.logic_gate as logic
def encrypt(plaintext: str, bit_op: str, key: str) -> str:
    cipher_text = ''
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        left = plaintext[:int(len(plaintext)/2)]
        right = plaintext[int(len(plaintext)/2):]
        
        encoder(bit_op, key, right)
        # print(right)
    return cipher_text
   
        
def encoder(bit_op: str, key: str, right: str):
    if bit_op == 'AND':
        encode = logic.and_op(key, right) 
        print(encode)
    elif bit_op == 'OR':
        encode = logic.or_op(key, right) 
        print(encode)
    elif bit_op == 'XOR':
        encode = logic.xor_op(key, right) 
        print(encode)
