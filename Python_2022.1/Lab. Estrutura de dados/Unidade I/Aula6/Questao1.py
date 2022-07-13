class Fila:
    def __init__(self):
        self.head = []

    def push(self, value):
        self.head.append(value)

    def pop(self):
       return self.head.pop(0)

    def isEmpty(self):
        if len(self.head) == 0:
            raise IndexError("Lista vazia")

    def imprimr(self):
        for i in range(len(self.head)):
            print(self.head[i])


class Pessoa:
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.conta = ''

    def append(self,nome, cpf,conta):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta


    def __str__(self):
        return (self.nome + ", " + self.cpf + ", " + self.conta)

f = Fila()
p = Pessoa()
p2 = Pessoa()
p.append("Adrier","700","Conta")
p2.append('Junior',"0000","10000")
f.push(p2)
f.push(p)
f.imprimr()













