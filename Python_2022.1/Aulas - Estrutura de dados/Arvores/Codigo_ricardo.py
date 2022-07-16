'''
Implementar uma tabela hash para armazenar informações de funcionários (nome e salário). 
A tabela tem tamanho M = 10, e a função de hash é dada por: 
Código ASCII da primeira letra do nome do funcionário % M
O tratamento de colisões é feito com o uso de listas. Podem ser usadas as listas do próprio Python.

O seu programa deve oferecer um menu com as seguintes opções:
1 - Inserir funcionário
2 - Buscar salário de um funcionário
0 - sair
'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho 
        self.list = [0] * tamanho
        for i in range(self.tamanho):
            self.list[i] = []

    def inserirFuncionario(self, funcionario):
        pos = ord(funcionario.nome[0]) % self.tamanho
        self.list[pos].append(funcionario)

    def buscarSalario(self, nome):
        pos = ord(nome[0]) % self.tamanho
        for funcionario in self.list[pos]:
            if funcionario.nome == nome:
                return funcionario.salario

    def imprimir(self):
        for linha in self.list:
            print ("> ", end='')
            for funcionario in linha:
                print(funcionario.nome, end=', ')
            print()


tabela = TabelaHash(10)

entrada = -1
while entrada != 0:
    print("-="*20)
    print('1 - Inserir funcionário')
    print('2 - Buscar salário de um funcionário')      
    print('3 - Imprimir toda a tabela')  
    print('0 - Sair')
    entrada = int(input('Escolha uma opcao: '))

    if entrada==1:
        nome = input('Digite o nome do novo funcionario: ')
        salario = float(input('Digite o salario do novo funcionario: '))
        funcionario = Funcionario(nome, salario)
        tabela.inserirFuncionario(funcionario)

    if entrada == 2:
        nome = input('Digite o nome do funcionario: ')
        salario = tabela.buscarSalario(nome)
        if not salario:
            print('Nao existe esse funcionario.')
        else:
            print(salario)

    if entrada == 3:
        tabela.imprimir()