def print_formatted(number):
    for i in range(number):
        if i != 0:
            print(str(i).replace("0b", " ").rjust(len(bin(number).replace("0b", "")), " "), end="")
            print(oct(i).replace("0o", "").rjust(len(bin(number).replace("0b", " ")), " "), end="")
            print(hex(i).replace("0x", "").upper().rjust(len(bin(number).replace("0b", " ")), " "), end="")
            print(bin(i).replace("0b", "").rjust(len(bin(number).replace("0b", " ")), " "))
    print(str(number).rjust(len(bin(number).replace("0b", "")), " "), end="")
    print(oct(number).replace("0o", "").rjust(len(bin(number).replace("0b", " ")), " "), end="")
    print(hex(number).replace("0x", "").upper().rjust(len(bin(number).replace("0b", " ")), " "), end="")
    print(bin(number).replace("0b", "").rjust(len(bin(number).replace("0b", " ")), " "))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)