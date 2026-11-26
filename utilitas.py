# utilitis.py - fungsi bantu

def format_hasil(operasi, a, b, hasil):
    return f"{a} {operasi} {b} = {hasil}"


def pangkat(a, b):
    return a ** b
# Penulis: Andi Rezky Nabila


def modulus(a, b):
    if b == 0:
        return "Error: modulus dengan nol"
    return a % b
