# Ordem:
# 1) insert
# 2) imprimir_pre
# 3_ imprimir centro
# 4) imprimir pos
# 5) tamanho
# 6) soma
# 7 altura
# 8) balanceada
# 9) gerar lista
# 10) destruir
# 11) gerar arvore
# 12) balanceamento estatico

class BSTNode:
    def __init__(self, value = None):
        self.data = value
        self.left = self.right = None
    
    def insert(self,value):
        if not self.data:
            self.data = value
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
    
    def imprimir_pre(self):
        if self.data:
            print(self.data, end=' ')  # processo o nó
            if self.left:  # vai para esquerda
                self.left.imprimir_pre()
            if self.right:  # vai para direita
                self.right.imprimir_pre()
    
    def imprime_central(self):
        if self.data:
            if self.left:
                self.left.imprime_central()
            print(self.data, end=',')
            if self.right:
                self.right.imprime_central()
    
    def imprime_pos(self):
        if self.data:
            if self.left:
                self.left.imprime_pos()
            if self.right:
                self.right.imprime_pos()
            print(self.data, end=',')

root = BSTNode()
root.insert(20)
root.insert(0)
root.insert(2)
root.insert(34)
root.insert(10)
root.imprimir_pre()

        