def cadastrar(tam):
    for i in range(tam):
        produto = input("Digite o produto: ")
        valor = input("Digite o valor:")
        if produto in dicionario:
            print("Já existe este produto na lista")
            parar = int(input("Deseja remover mais algum produto? Digite 0 para NÃO e 1 para SIM: "))
            if parar == 1:
                cadastrar(1)

        else:
            dicionario[produto] = valor

def remover():
    parar = -1
    while parar != 0:
        produtoRemo = input("Digite o produto que você deseja remover:")
        if produtoRemo in dicionario:
            dicionario.pop(produtoRemo)
        else:
            print("O produto não está cadastrato")
        parar = int(input("Deseja tenter novamente? Digite 0 para NÃO e 1 para SIM: "))

def pesquisar():
    parar = -1
    while parar != 0:
        produto = input("Digite o produto que deseja pesquisar: ")
        if produto in dicionario:
            print("Nome: ", produto, "\nValor: R$", dicionario.get(produto), )
        else:
            print("O produto não está cadastrado!")
        parar = int(input("\nDeseja buscar mais um produto? Digite 0 para NÃO e 1 para SIM: "))

def imprime():
    for k,v in dicionario.items():
        print(k,"- R$",v)

def switch():
    parada = 0
    while parada != -1:
        case = int(input("1-Cadastrar produtos\n"
                         "2-Pesquisar produtos\n"
                         "3-Remover produtos\n"
                         "4-Imprimir produtos cadastrados\n"
                         "5-Para sair\n"
                         ":"))
        if case == 1:
            tam = int(input("Digite quantos produtos irá cadastrar: "))
            cadastrar(tam)
        elif case == 2:
            pesquisar()
        elif case == 3:
            remover()
        elif case == 4:
            imprime()
        elif case == 5:
            parada = -1
        else:
            print("Opção inválida")

dicionario = {}
switch()


