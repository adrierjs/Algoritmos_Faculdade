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

    def concatenar(self, lista2):
        self.append(lista2)


    def listaIntercalada(self, lista2):
        tam1 = self.__size
        tam2 = lista2.__size
        novaLista = []
        if (self.head and lista2.head):
            if (tam1 == tam2):
                for i in range(tam1):
                    novaLista.append(self[i])
                    novaLista.append(lista2[i])
        else:
            raise IndexError('Lista vazia')

        print(novaLista)



    def __str__(self):
        output = '['
        aux = self.head
        while aux:
            output += str(aux.data)
            if aux.next:
                output += ' , '
            aux = aux.next
        output += ']'
        return output

l1 = LinkedList()
l1.append(1)
l1.append(2)
l2 = LinkedList()
l2.append(3)
l2.append(4)
l1.listaIntercalada(l2)


