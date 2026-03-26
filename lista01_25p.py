#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
#meu Deus como que faz isso

hi:int=0 #hora inicial
mi:int=0 #minuto inciia
hf:int=0 #hora final
mf:int=0 #minuto final
dt:int=0 #duração total
it:int=0 #inicio total
ft:int=0 #fim totaç
dh:int=0 #duração horas
dm:int=0 #duração min

def calc():
    global hi, mi, hf, mf, it, dt
  
    it = hi * 60 + mi
    ft = hf * 60 + mi

    if ft < it:
       
        dt = (24 * 60 - it) + ft
    else:
        dt = ft - it

    dh = dt // 60
    dm = dt % 60

    print("duraçao do jogo: ",dh," horas e", dm," minutos")
def main():
    global hi, mi, hf, mf, dt, ft, it
    hi = int(input("Hora de inicio HH: "))
    mi = int(input("Minuto de inicio MM: "))
    hf = int(input("Hora de fim HH: "))
    mf = int(input("Minuto de fim MM: "))
    calc()

if __name__ == "__main__":
    main()