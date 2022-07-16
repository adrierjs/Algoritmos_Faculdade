class BSTNode:
    def __init__(self, value=None):
        self.data = value
        self.left = self.right = None

    def insert(self, value):
        if not self.data:
            self.data = value

        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def pre_ordem(self):
        if self.data:
            print(self.data, end=' ')
            if self.left:
                self.left.pre_ordem()
            if self.right:
                self.right.pre_ordem()

    def ordem_central(self):
        if self.data:
            if self.left:
                self.left.ordem_central()
            print(self.data, end=' ')
            if self.right:
                self.right.pre_ordem()

    def pos_ordem(self):
        if self.data:
            if self.left:
                self.left.pos_ordem()
            if self.right:
                self.right.pos_ordem()
            print(self.data, end == ' ')

    def tamanho(self):
        if not self.data:
            return 0
        else:
            if self.left:
                esq = self.left.tamanho()
            else:
                esq = 0
            if self.right:
                dir = self.right.tamanho()
            else:
                dir = 0

        return esq + dir + 1

    def soma_graus(self):
        if not self.data:
            return 0
        else:
            if self.left:
                s_left = self.left.soma_graus()
            else:
                s_left = 0
            if self.right:
                s_right = self.right.soma_graus()
            else:
                s_right = 0

        return s_left + s_right + self.data

    def altura(self):
        if not self.data:
            return -1
        else:
            if self.left:
                a_erq = self.left.altura()
            else:
                a_erq = 0
            if self.right:
                a_dir = self.right.altura()
            else:
                a_dir = 0
        if a_erq < a_dir:
            return a_erq + 1
        else:
            return a_dir+1

    def inserir_lista(self, lista):
        if self.data:
            if self.left:
                self.left.inserir_lista(lista)
            lista.append(self.data)
            if self.right:
                self.right.inserir_lista(lista)

    def deletar_ar(self):
        if self.data:
            if self.left:
                self.left.deletar_ar()
            if self.right:
                self.right.deletar_ar()
            del self.data
            del self


root = BSTNode()
root.insert(10)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(20)
root.insert(25)
root.insert(13)
root.insert(2)
print('Pré ordem:')
root.pre_ordem()
print('\nOrdem central:')
root.ordem_central()
print('Tamanho:', root.tamanho())
print('Soma graus:', root.soma_graus())
print('Altura:', root.altura())
lista = []
root.inserir_lista(lista)
print(lista)
root.deletar_ar()
