def and_op(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError
    
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) and int(b[i]))
    return result
 
    
def or_op(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError
    
    result = "" 
    for i in range(len(a)):
        result += str(int(a[i]) or int(b[i]))
    return result     


def xor_op(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError
    
    result = "" 
    for i in range(len(a)):
        result += str(int(a[i]) != int(b[i])) 
    # return result  
    return result 
    
    
and_op('0011', '1101')