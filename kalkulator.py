# kalkulator.py - Kalkulator sederhana
from bantuan import format_hasil


def tambah(a, b):
    return a + b


if __name__ == "__main__":
    print("Kalkulator Sederhana")
    print(format_hasil("+", 2, 3, tambah(2, 3)))
