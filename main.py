import logic_gate as logic
def encrypt(plaintext: str, bit_op: str, key: str):
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        left = plaintext[:int(len(plaintext)/2)]
        right = plaintext[int(len(plaintext)/2):]
        
        