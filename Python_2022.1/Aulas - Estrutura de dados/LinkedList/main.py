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
    self.__size += 1

  def __len__(self):
    return self.__size

  def __getitem__(self, index):
    pass
    #if self.head:
    #  pass
    #else:
    #  raise IndexError('Lista vazia.')
  
  
l = LinkedList()
l.append(100)
l.append(200)
print(len(l))
print(l[0])


lista = []
lista.append(10)
print(lista[0])