#18 ache a diferença do numero maior

a: int = 0
b: int = 0
r: int = 0


def dif():
    global a, b, r
    if a > b:
        r = a - b
    else:
        r = b - a
    print(r)

def main():
    global a, b
    #^^^lembre de declarar globais dentro do tchere thce tche main senao num vai dar!!!
    a = int(input('Entre o valor 1: '))
    b = int(input('Entre o valor 2: '))
    dif()

if (__name__ == "__main__"):
    main()