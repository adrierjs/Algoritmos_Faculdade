class Pessoa:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setSalario(self, salario):
        self.__salario = salario

    def getSalario(self):
        return self.__salario

class Hash:
    def __init__(self):
        self.lista = [0]*10

        for i in range(10):
            self.lista[i] = []

    def insert(self, pessoa):
        ascii = ord(pessoa.getNome()[0])
        pos = ascii % 10
        self.lista[pos].append(pessoa)

    def buscarSalario(self,nome):
        ascii = ord(nome[0])
        pos = ascii % 10
        for nome_e in self.lista[pos]:
            if nome_e.getNome() == nome:
                return nome_e.getSalario()

    def imprimir(self):
        for i in self.lista:
            print('-', end=' ')
            for funcionario in i:
                print(funcionario.getNome(), end=',')

tabela = Hash()

def menu():
    print('1 - Inserir funcionário',
    '\n2 - Buscar salário de um funcionário',
    '\n0 - sair')

entrada = -1
t1 = Hash()
verificacao = False
while entrada != 0:
    menu()
    entrada = int(input('Digite: '))
    if entrada == 1:
        nome = input('Digite o nome do funcionário: ')
        salario = float(input('Digite o salário do funcionário: '))
        p1 = Pessoa(nome, salario)
        t1.insert(p1)
        verificacao = True

    elif entrada == 2:
        if verificacao:
            nome = input('Digite o nome do funcionário: ')
            salario = t1.buscarSalario(nome)
            if not salario:
                print('O usuário não foi encontrado!')
            else:
                print('R$:', salario)
        else:
            print('Não tem nenhum usuário inserido!')

    elif entrada == 0:
        entrada = 0
    elif entrada == 3:
        t1.imprimir()
    else:
        print('Opção incorreta!')

