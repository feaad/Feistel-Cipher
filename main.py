
def encrypt(plaintext):
    if len(plaintext) % 2 != 0:
        print("Input must even")
    else:
        left = plaintext[:int(len(plaintext)/2)]
        right = plaintext[int(len(plaintext)/2):]