class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self, value):
        if (self.head):
            aux = self.head
            while (aux.next):
                aux = aux.next
            aux.next = Node(value)

        else:
            self.head = Node(value)
        self.__size += 1

    def __len__(self):
        return self.__size

    def __getitem__(self, index):
        if(self.head):
            aux = self.head
            if aux.next:
                for i in range(index):
                    aux = aux.next
                return aux.data
            else:
                raise IndexError('O elemento não está na lista')
        else:
            raise IndexError('Lista vazia')

    def retornaPrimeira(self, value):
        if self.head:
            tam = self.__size
            for i in range(tam):
                if self[i] == value:
                    return i
            else:
                return ('O valor não está na lista')
        else:
            raise IndexError('Lista vazia')

    def __getitem__(self, index):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Indice fora da lista')
            return aux.data
        else:
            raise IndexError('Lista vazia')

l = LinkedList()
l.append(20)
l.append(30)
l.append(12)
l.append(45)
print("A primeira posição que o valor se encontra é:",l.retornaPrimeira(45))





