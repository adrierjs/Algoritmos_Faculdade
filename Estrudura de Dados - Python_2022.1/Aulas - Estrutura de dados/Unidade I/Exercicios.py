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
                aux = aux.next
            return aux.data
        else:
            raise IndexError('Lista vazia')

    def __setitem__(self, index, value):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux.next = aux
                else:
                    raise IndexError('Item fora da lista')
            aux.data = value
        else:
            raise IndexError('Lista vazia')

    def __len(self):
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

    def removeUltimo(self):
        if self.head:
            aux = self.head
            aux2 = aux
            while aux.next:
                aux2 = aux
                aux = aux.next
            if aux2 == None:
                del aux
            else:
                aux2.next = None
                del aux2

    def removePrimeiro(self):
        if self.head:
            if self.head.next:
                aux = self.head
                self.head = aux.next
                aux.next = None
                del aux
            else:
                del self.head
                self.head = None

        else:
            raise IndexError('Lista vazia')






# l = LinkedList()
# l.append(20)
# l.append(30)
# l.append(22)
# l.append(12)
#
#
#
# print(l)

dicionario = {}

dicionario.__setitem__("Adrier",10)
print(dicionario.keys()) #retorna somente as chaves
print(dicionario.values()) #valor
print(dicionario.get("Adrier")) #retorna do valor da chave fornecida


