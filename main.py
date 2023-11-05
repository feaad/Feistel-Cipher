import logic_gate as logic
def encrypt(plaintext: str, bit_op: str, key: str):
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        left = plaintext[:int(len(plaintext)/2)]
        right = plaintext[int(len(plaintext)/2):]
        
        encoder(bit_op, key, right)
        # print(right)
        

def encoder(bit_op: str, key: str, right: str):
    if bit_op == 'AND':
        encode = logic.and_op(key, right) 
        print(encode)


encrypt('10010011', 'AND', '1101')