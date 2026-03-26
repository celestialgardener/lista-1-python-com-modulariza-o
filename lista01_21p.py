#receba 4 notas bimestrais de um aluno calcule e mostre a media aritiemtica e mostre a mensagem de acordo
n1:int=0
n2:int=0
n3:int=0
n4:int=0
m:int=0
def main():
    global n1,n2,n3,n4,m 
    n1 = int(input('entre a primeira nota'))
    n2 = int(input('entre a segunda nota'))
    n3 = int(input('entre a terceira nota'))
    n4 = int(input('entre a quarta nota'))
    media()


def media():
    global n1,n2,n3,n4,m 
    m = (n1+n2+n3+n4)/4
    print('a média do aluno foi',m)
    if m>=6:
        print('aprovado')
    if m>=3 and m<6:
        print('exame')
    if m<3:
        print('retido')

if (__name__ == "__main__"):
    main()
