class Node:  # clase node - para adicionar um número
    def __init__(self, value):  # construtor para inicializar o nó
        self.data = value  # self.data recebe algum valor
        self.next = None  # o proximo valor é none


class LinkedList:
    def __init__(self):
        self.head = None  # a cabeça começa vazia
        self.__size = 0  # tamanho do tipo privado inica em 0

    def append(self, value):  # adicionar valor
        if self.head:  # se tiver algo na cabeça
            aux = self.head  # aux recebe a cabeça
            while aux.next:  # enquanto tiver algo em aux
                aux = aux.next  # aux recebe o proximo
            aux.next = Node(value)  # aux proximo recebe o valor que vem na função node
        else:  # se nao tiver nada na cabeça
            self.head = Node(value)  # a cabeça recebe nó
        self.__size += 1

    def removerPrimeiro(self):
        if (self.head):
            if (self.head.next):  # se tiver mais de um dado
                aux = self.head  # aux recebe o inicio
                self.head = aux.next  # o inicio passa a ser o proximo
                aux.next = None  # o proximo sera None
                del aux  # deleta o aux
            else:  # se tiver so um dado
                del self.head  # deleta o começo
                self.head = None  # e aponta para none
        else:
            raise IndexError('Lista vazia')

    def removeUltimo(self):
        if (self.head):
            aux1 = self.head
            aux2 = aux1
            while (aux1.next):
                aux2 = aux1
                aux1 = aux1.next
            if (aux2 == None):
                del aux1
                self.head = None
            else:
                aux2.next = None
                del aux1

        else:
            raise IndexError('Lista vazia')  # a cabeça recebe nó

    def verificarPar(self):

        if self.head:
            aux = self.head
            while aux:
                if (aux.data % 2 == 0):
                    print(aux.data)
                aux = aux.next

        else:
            raise IndexError('Lista vazia')

    def __len__(self):
        return self.__size

    def __getitem__(self, index):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Lista vazia')
            return aux.data
        else:
            raise IndexError('Lista vazia.')

    def __setitem__(self, index, value):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Lista vazia')
            aux.data = value
        else:
            raise IndexError('Lista vazia.')

    def __str__(self):
        output = '['
        aux = self.head
        while aux:
            output += str(aux.data)
            if aux.next:
                output += ', '
            aux = aux.next
        output += ']'
        return output


l = LinkedList()


l.append(20)
print(l.__len__())
# print(len(l)
print(l[0])
# print(l[0])
# l[0] = 170
# print(l[0])

# lista = []
# lista.append(10)
# print(lista[0])
