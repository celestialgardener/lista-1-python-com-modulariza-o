#receba dois valores inteiros e diferentes mostre seus valores em ordem crescente
a: int=0
b:int=0
def main():
    global a,b
    a=int(input('entre o valor a'))
    b=int(input('entre o valor b'))
    conta()

def conta():
    global a,b
    if a>b:
        print(b)
        print(a)
    if b>a:
        print(a)
        print(b)



if (__name__ == "__main__"):
    main()
