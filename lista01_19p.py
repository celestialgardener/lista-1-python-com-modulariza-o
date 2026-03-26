#19

a:int= 0
b:int= 0

def maior():
    global a, b
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Valores iguais")

def main():
    global a, b
    a = int(input('entre o valor 1: '))
    b = int(input('entre o valor 2: '))
    
    maior()

if (__name__ == "__main__"):
    main()

    