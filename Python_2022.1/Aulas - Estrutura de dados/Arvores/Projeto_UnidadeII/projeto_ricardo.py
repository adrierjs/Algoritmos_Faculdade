class Pessoa:
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario

class Tabela:
    def __init__(self):
        self.tamanho = 10
        self.lista = [0]*self.tamanho

        for i in range(self.tamanho):
            self.lista[i] = []

    def insert(self, Pessoa):
        ascii = ord(Pessoa.nome[0])
        codigo = ascii%2
        self.lista[codigo].append(ascii)

    def imprimir(self,nome):
        for nome in self.lista:
            print(self.lista[nome])


p1 = Pessoa('Adrier',1000)
p2 = Pessoa('Angelo',2000)
t1 = Tabela()
t1.insert(p1)
t1.imprimir('Adrier')

