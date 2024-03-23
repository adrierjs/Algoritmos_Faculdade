class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
  def __init__(self):
    self.head = []

  def push(self,value):
    self.head.append(value)

  def pop(self):
     return self.head.pop()

  def isEmpty(self):
    return len(self.head) == 0

class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self, value):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Node(value)

        else:
            self.head = Node(value)
        self.__size +=1

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
        if (self.head):
            aux = self.head
            for i in range(index):
                if (self.head):
                    aux = aux.next
                else:
                    raise IndexError('Elemento fora da lista')
            aux.data = value
        else:
            raise IndexError('Lista vazia')

    def __len__(self):
        return self.__size

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

    #Questao1
    def extend(self, lista):
        tam = lista.__len__()
        for i in range(tam):
            self.append(lista.__getitem__(i))

    # Questao2
    def insert(self, index, value):
        tam = self.__len__()
        aux = LinkedList()
        for i in range(index, tam):
            aux.append(self.__getitem__(i))
            self.__setitem__(index,value)
        if index >= tam:
            l.append(value)
        self.extend(aux)
        return self

#começo da questao 3
    def pop(self):
        if self.head: #se nao tiver nada na lista
            aux = self.head
            while aux.next:
                ant = aux
                aux = aux.next
            del aux
            ant.next = None
        elif not self.head.next:
            del self.head
            self.head = None
        else:
            raise IndexError('Lista vazia')

    def pop(self,index):
        if self.__size < index:
            raise IndexError('Lista vazia')

        elif index == 0:
            aux = self.head
            self.head = self.head.next
            del aux
        else:
            aux = self.head
            for i in range(index):
                ant = aux
                aux = aux.next
            ant.next = aux.next
            del aux


#Questão 4
    def print_partial(self,tam1,tam2):
        listaAux = LinkedList()
        if 0 > tam1 or self.__size < tam2:
            return 'Fora da lista'
        for i in range(tam1, tam2):
            listaAux.append(self[i])

        return listaAux

    # def inverse(self):
    #     pilha = Stack()
    #     lista = LinkedList()
    #     for i in range(len(self)):
    #         pilha.push(self[i])
    #
    #     for i in range(len(self)):
    #         lista.append(pilha.pop())
    #
    #     return lista

    def inverse(self):
        pilha = Stack()
        aux = self.head
        for i in range(len(self)):
            pilha.push(aux.data)
            aux = aux.next
        for i in range(len(self)):
            self.pop(i)
        while not pilha.isEmpty() == 0:
            self.append(pilha.pop())
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(5)
l.pop()


