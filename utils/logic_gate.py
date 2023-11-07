def and_op(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError

    result = ""
    for i in range(len(a)):
        result += str(int(a[i] and b[i]))
    return result


def or_op(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError

    result = ""
    for i in range(len(a)):
        result += str(int(a[i] or b[i]))
    return result


def xor_op(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError

    result = ""
    for i in range(len(a)):
        result += str(int(a[i] != b[i]))
    return result
