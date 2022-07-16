class BSTnode:
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
                self.left = BSTnode(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTnode(value)

    def imprimir_pre(self):
        if self.data:
            print(self.data, end=' ')
            if self.left:
                self.left.imprimir_pre()
            if self.right:
                self.right.imprimir_pre()

    def imprimir_central(self):
        if self.data:
            if self.left:
                self.left.imprimir_central()
            print(self.data, end=' ')
            if self.right:
                self.right.imprimir_central()

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

    def balanceada(self):
        if not self.data:
            return True
        else:
            x = self.left.balanceada() if self.left else True
            y = self.right.balanceada() if self.right else True
            a = self.left.altura() if self.left else -1
            b = self.right.altura() if self.right else -1
            z = abs(a-b) <= 1
            return x and y and z

    def gerar_lista(self, lista):
        if self.data:
            if self.left:
                self.left.gerar_lista(lista)
            lista.append(self.data)
            if self.right:
                self.right.gerar_lista(lista)

    def destruir(self):
        if self.data:
            if self.left:
                self.left.destruir()
            if self.right:
                self.right.destruir()
            del self.data
            del self

    def gerar_arvore(self, lista, ini, fim):  # INCOMPLETO
        meio = (ini + fim) // 2
        self.data = lista[meio]
        if ini <= meio-1:
            self.left = BSTnode()    
            self.left.gerar_arvore(lista, ini, meio-1)
        else:
            self.left = None
        if meio+1 <= fim:
            self.right = BSTnode()
            self.right.gerar_arvore(lista, meio+1, fim)
        else:
            self.right = None

    def balanceamento_estatico(self):
        if not self.balanceada():
            l = []
            self.gerar_lista(l)
            self.destruir()
            self = BSTnode()
            self.gerar_arvore(l,0,len(l)-1)
        return self

root = BSTnode()
root.insert(10)
root.insert(20)
root.insert(30)
root.insert(40)
root.insert(50)
root.insert(60)
root.insert(70)
root.insert(80)
# print('Pre-ordem:', end=' ')
# root.imprimir_pre()
# print('\nOrdem central: ', end=' ')
# root.imprimir_central()
# print('\nTamanho:', root.tamanho())
# print('Soma:', root.soma())
print('Altura:', root.altura())
print('Balanceada: ', root.balanceada())
root = root.balanceamento_estatico()
print('Altura:', root.altura())
print('Balanceada: ', root.balanceada())
root.imprimir_central()
