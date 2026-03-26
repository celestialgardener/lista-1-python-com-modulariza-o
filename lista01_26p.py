#receba dois numeros verifique se o maor é multiplo do menor
#esse aqui é fim dos exercicios com vaiavel global
a:int=0
b:int=0
menor:int=0
maior:int=0

def mult():
    global a,b,menor
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    if menor == 0:
        print("dividir por zero NAO SERA TOLERADO!!!!!!")
        return

    if maior % menor == 0:
        print(maior," é multiplo de ",menor)
    else:
        print(maior,"não é multiplo de",menor)

def main():
    global a,b,maior,menor
    a = int(input("numero 1: "))
    b = int(input("numero 2: "))
    mult()

if (__name__ == "__main__"):
    main()