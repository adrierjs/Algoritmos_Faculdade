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


    def __len__(self):
        return self.__size

    def __setitem__(self, index, value):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Fora da lista')

            aux.data = value
        else:
            raise IndexError('Lista vazia')

    def __getitem__(self, index):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Fora da lista')
            return aux.data
        else:
            raise IndexError('Lista vazia')

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


    def pop(self):
        if self.head:
            aux = self.head
            aux2 = aux
            while aux.next:
                aux2 = aux
                aux = aux.next
            if aux2.next == None: #é porque só tem um elemento
                del aux
                self.head = None
            else:
                aux2.next = None
                del aux

    def removePrimeiro(self):
        if self.head:
            if self.head.next:
                aux = self.head
                self.head = aux.next
                aux.next = None
                del aux
            else:
                self.head = None
                del self.head
        else:
            raise IndexError('Lista vazia')

l = LinkedList()
l.append(20)
l.__setitem__(0,21)
l.append(30)
l.append(21)
l.removePrimeiro()

print(l.__str__())



