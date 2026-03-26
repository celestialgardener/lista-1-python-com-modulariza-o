#receba o tipo de investimento 1 poupança 2 renda fixa e o valor calcule e mostre o valor corrigido em 30 dias sabendo que poupança = 3% e renda fixa 5%
tipo:int=0
valor:int=0
nv:int=0

def main():
    tipo = int(input("digite o tipo de investimento 1 poupança 2 renda fixa "))
    valor = int(input("digite o valor"))
    calc(tipo, valor)


def calc(tipo, valor):
    if tipo == 1:
        nv = valor * 1.03
    if tipo == 2:
        nv = valor * 1.05  
    else:
        print("tipo não existe")
        return
    print("valor corrigido ",nv)


if (__name__ == "__main__"):
    main()