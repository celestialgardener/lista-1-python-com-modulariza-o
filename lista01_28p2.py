#28 receba o preço atual e a media mensal de vendas do produto  cacule o novo preco sabendo das informações de venda
vm:int=0
pa:int=0
pn:int=0


def main():
    vm = int(input('qual a media mensal'))
    pa = int(input('qual o preço atual do produto '))
    conta(vm, pa)

def conta(vm, pa):
    if vm < 500 and pa < 30:
        pn = pa * 1.10
        print(pn)
    elif vm >= 500 and vm < 1000 and pa >= 30 and pa < 80:
        pn = pa * 1.15  
        print(pn)
    elif vm >= 1000 and pa > 80:
        pn = pa - (pa * 0.05)
        print(pn)
    else:
        print('preço igual')

if (__name__ == "__main__"):
    main()