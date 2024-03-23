class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self,value):
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
            controle = 0
            aux = self.head
            while controle != 0:
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Item fora da lista')
            return aux.data
        else:
            raise IndexError('Lista vazia')

    def __setitem__(self, index,value):
        if self.head:
            controle = 0
            aux = self.head
            while controle != index :
                aux = aux.next
            aux.data = value

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

    def ordena_vet(self):
        tam = self.__len__()
        aux = []
        for j in range(tam):
            for i in range(tam):
                if (self[i] > self[i + 1]):
                    aux.append(self[i])
                    self.append(self[i+1])

                    self.append(aux)
        return self

l = LinkedList()
l.append(5)
l.append(2)
print(l.ordena_vet())
