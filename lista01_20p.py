#receber os 3 coeficientes A B e C de uma equação de 2 grau da fomula ax²+bx+c=0 e mostre a existencia de raizes reais e se caso existem mostre
a:int=0
b:int=0
c:int=0
raiz1: int=0
raiz2: int=0
delta: int=0
def main():
    global a,b,c,raiz1,raiz2,delta
    a = int(input('entre o valor a'))
    b = int(input('entre o valor b'))
    c = int(input('entre o valor c'))
    delta = b**2 - 4*a*c
    conta()


def conta():
    global a,b,c,raiz1,raiz2,delta
    if delta >=0:
        raiz1 = (-b+ (delta**0.5)) / 2*a
        raiz2 = (-b- (delta**0.5)) / 2*a
        print(raiz1)
        print(raiz2)
    if delta < 0:
        print('não ha raizes reais')



if (__name__ == "__main__"):
    main()
