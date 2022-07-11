class BSTnode:
    def __init__(self, value=None): #incia nem nada só apenas p criar um nó
        self.data = value  #self.data recebe o valor
        self.left = self.right = None #Esquerda e direita recebem nulo porque ainda não inseriu um filho

    def insert(self, value):
        if not self.data: #se não tiver nada em self.data
            self.data = value #self.data recebe valor
        elif value < self.data: #valor for menor que self.data
            if self.left: #se tiver algo na esquerda
                self.left.insert(value) #a esquerda recebe um valor
            else:
                self.left = BSTnode(value) #se não tiver nada, cria um nó na esquerda
        elif value > self.data: #se o valor for maior que o self.data
            if self.right: #se tiver algo na direita
                self.right.insert(value) #a direita recebe um novo valor
            else: #se não tiver nada na direita, cria um novo nó
                self.right = BSTnode(value) #se não tiver nada na direita, cria um novo nó

    def imprimir_pre(self):
        if self.data:
            print(self.data, end=' ') #processo o nó
            if self.left: #vai para esquerda
                self.left.imprimir_pre()
            if self.right: #vai para direita
                self.right.imprimir_pre()

    def imprimir_central(self):
        if self.data:
            if self.left:
                self.left.imprimir_central()
            print(self.data, end=' ')
            if self.right:
                self.right.imprimir_central()

    def imprimir_pos(self):
        if self.data:
            if self.left:
                self.left.imprimir_pos()
            if self.right:
                self.right.imprimir_pos()
            print(self.data, end=' ')

    # def tamanho(self):
    #     if not self.data:
    #         return 0
    #     else:
    #         if self.left:
    #             esq = self.left.tamanho()
    #         else:
    #             esq = 0
    #         if self.right:
    #             dir = self.right.tamanho()
    #         else:
    #             dir = 0
    #         return esq + dir + 1

    def soma_d(self):
        if not self.data:
            return 0
        else:
            if self.left:
                esq = self.left.soma_d()
            else:
                esq = 0
            if self.right:
                dir = self.right.soma_d()
            else:
                dir = 0
            return esq + dir + self.data

    def tamanho(self):
        if not self.data:
            return 0
        else:
            return (self.left.tamanho() if self.left else 0) + (self.right.tamanho() if self.right else 0) + 1

    def soma(self):
        if not self.data:
            return 0
        else:
            return (self.left.soma() if self.left else 0) + (self.right.soma() if self.right else 0) + self.data

    def altura(self):
        if not self.data:
            return -1
        else:
            alt_e = self.left.altura() if self.left else -1
            alt_d = self.right.altura() if self.right else -1
            return alt_e + 1 if alt_e > alt_d else alt_d + 1


root = BSTnode()
root.insert(10)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(20)
root.insert(25)
root.insert(13)
root.insert(2)
print('Pre-ordem:', end=' ')
root.imprimir_pre()
print('\nOrdem central: ', end=' ')
root.imprimir_central()
print('\nPós ordem: ', end=' ')
root.imprimir_pos()

print('\nTamanho:', root.tamanho())
print('Soma:', root.soma())

print('Altura:', root.altura())



