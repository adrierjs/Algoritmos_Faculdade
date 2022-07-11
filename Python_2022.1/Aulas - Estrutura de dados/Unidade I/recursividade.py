def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)  # chame a função de novo e faça o número antecessor


def fatorialWhile(n):
    while n != 0:
        return n * fatorialWhile(n - 1)
    return 1

def fibo(posicao):
    if posicao == 1 or posicao ==2:
        return 1
    else:
        return fibo(posicao-1)+fibo(posicao-2)


print(fibo(6))

def notas(tam):
    nota = []*tam

    for i in range(tam):
        n = float(input("Digite a nota "))
        nota.append(n)

    return nota

def soma(tam):
    media = 0
    n1 = notas(tam)
    for i in range(tam):
        media +=n1[i]
    media = (media/tam)
    print("A média foi: %.2f"%media)

#print(fatorialWhile(7))

soma(int(input("Digite o tamanho")))

