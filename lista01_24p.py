#receba um valor inteiro, verifique se ele é divisivel por 2 e 3
valor : int=0
def main():
    global valor
    valor = int(input('entre o valor pra ver se ele é divisivel por 2 e 3'))
    conta()

def conta():
    global valor
    if valor % 3 != 0 or valor% 2 != 0:
        print('valor nao divisivel por 2 e 3')

    if valor % 3 == 0 and valor% 2 == 0:
        print('valor divisivel por 2 e 3')


if (__name__ == "__main__"):
    main()

