class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

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

    def __setitem__(self,index, value):
        if self.head:
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Fora da lista')
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

    def extend(self, lista):
        tam = lista.__len__()
        for i in range(tam):
            self.append(lista.__getitem__(i))

    # Questao2
    def insert(self):
        pass

    def pop(self):







l = LinkedList()
l2 = LinkedList()
l.append(20)
l2.append(30)
l2.append(10)
l2.append(13)
l.extend(l2)
print(l)


