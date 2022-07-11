class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self, value):
        if(self.head):
            aux = self.head
            while(aux.next):
                aux = aux.next
            aux.next = Node(value)
        else:
            self.head = Node(value)
        self.__size +=1

    def __len__(self):
        return self.__size

    def concatenar(self, lista2):
        self.append(lista2)
        # if(self.head):
        #     aux = self.head
        #     while (aux.next):
        #         aux = aux.next
        #
        #     aux.next = Node(lista2)
        #
        # else:
        #     self.head = Node(lista2)
        # self.__size +=1


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
l.append(2)
l2 = LinkedList()
l2.append(5)
# l.append(20)
# l.append(10)
l.concatenar(l2)
print(l)
