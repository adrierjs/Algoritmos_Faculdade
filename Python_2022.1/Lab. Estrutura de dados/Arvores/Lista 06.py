class BSTnode:
    def __init__(self, value = None):
        self.data = value
        self.left = self.right = None


    def insert(self, value):
        if not self.data:
            self.data = value
        elif value < self.data:
            if not self.left:
                self.left = BSTnode(value)
            else:
                if self.left:
                    self.left.insert(value)
        elif value > self.data:
            if not self.right:
                self.right = BSTnode(value)
            else:
                if self.right:
                    self.right.insert(value)

    def soma_graus(self):
        if self.data:
            grau = 0
            if self.left:
                grau +=1
                self.left.soma_graus()
            if self.right:
                grau +=1
                self.right.soma_graus()
            print('Nó:', self.data, end=' - ')
            print('Grau:',grau)


    def contar_folhas(self):
        if not self:
            return 0
        elif not self.left and not self.right:
            return 1
        else:
            if self.left:
                esq = self.left.contar_folhas()
            else:
                esq =  0
            if self.right:
                dir = self.right.contar_folhas()
            else:
                dir = 0
            return esq + dir






root = BSTnode()
root.insert(10)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(20)
root.insert(25)
root.insert(13)
root.insert(2)
print(root.contar_folhas())







