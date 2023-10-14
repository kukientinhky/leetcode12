def f1(n):
    if n == 1:
        return "C"
    elif n == 2:
        return  "CC"
    elif n == 3:
        return "CCC"
    elif n == 4:
        return "CD"
    elif n == 5:
        return "D"
    elif n == 6:
        return "DC"
    elif n == 7:
        return "DCC"
    elif n == 8:
        return "DCCC"
    elif n == 9:
        return "CM"
def f2(n):
    if n == 1:
        return "X"
    elif n == 2:
        return "XX"
    elif n == 3:
        return "XXX"
    elif n == 4:
        return "XL"
    elif n == 5:
        return "L"
    elif n == 6:
        return "LX"
    elif n == 7:
        return "LXX"
    elif n == 8:
        return "LXXX"
    elif n == 9:
        return "XC"
def f3(n):
    if n == 1:
        return "I"
    elif n == 2:
        return "II"
    elif n == 3:
        return "III"
    elif n == 4:
        return "IV"
    elif n == 5:
        return "V"
    elif n == 6:
        return "VI"
    elif n == 7:
        return "VII"
    elif n == 8:
        return "VIII"
    elif n == 9:
        return "IX"
def main():
    str = ""
    num = 1999
    n = num // 1000
    for i in range(n):
        str = str + "M"
    num = num % 1000
    n = num // 100
    if f1(n) is not None:
        str = str + f1(n)
    num = num % 100
    n = num // 10
    if f2(n) is not None:
        str = str + f2(n)
    num = num % 10
    n = num
    if f3(n) is not None:
        str = str + f3(n)
    print(str)
if __name__ == "__main__":
    main()