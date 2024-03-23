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

    def removerUltimo(self):
        if self.head:
            aux = self.head
            self.head = aux.next
            aux.next = None
            del aux
        else:
            del self.head
            self.head = None

l = LinkedList()
l.append(20)
l.append(10)
print(l)
l.removerUltimo()
print(l)


