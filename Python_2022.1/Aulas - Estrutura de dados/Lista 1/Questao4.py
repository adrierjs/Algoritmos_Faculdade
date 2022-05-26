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

    def __get__(self, index):
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


