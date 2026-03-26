#esses exercicios tem que fazer com procedimentos em Python COM PASSAGEM DE
#PARÃMETROS (Com variáveis locais). Os exercícios devem ser organizados com chamada
#de main para a parte principal do código e a modularização.
#NAO pode escrever global e tem que passar os parametros a serem usados no tchongo 

#27 recceba o numero de voltas extensao do circuito em metros e o tempo de duração em minutos calcule a velocidade media em khm/h

voltas:int=0
tamanho:int=0
tempo:int=0
vm:int=0

def main():
    voltas = int(input('quantas voltas deu'))
    tamanho = int(input('qual o tamanho do circuito'))
    tempo = int(input('quantas quanto tempo levou'))
    calc(voltas,tamanho,tempo)

def calc(voltas,tamanho,tempo):
    vm = (voltas * tamanho * 60) / (tempo * 1000)
    print(vm)


if (__name__ == "__main__"):
    main()
    