#supermercado


def cadastrar(tam):
    for i in range(tam):
        produto = input('Digite o nome do produto:')
        valor= float(input("Digite o valor do produto: "))
        dicionario[produto] = valor


dicionario = {}
cadastrar(1)
