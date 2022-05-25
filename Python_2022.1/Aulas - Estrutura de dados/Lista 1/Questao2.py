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

  def __len__(self):
    return self.__size


  def divideLista(lista):
    tamt = lista.__len__()
    tam = (tamt / 2)
    novaLista1 = []
    novaLista2 = []
    if tamt % 2 == 0:
      for i in range(0,int(tam)):
        novaLista1.append(lista.__getitem__(i))

      for i in range(int(tam), tamt):
        novaLista2.append(lista.__getitem__(i))

    else:
      for i in range(0, int(tam+1)):
        novaLista1.append(lista.__getitem__(i))

      for i in range(int(tam+1), tamt):
        novaLista2.append(lista.__getitem__(i))

    print(novaLista1)
    print(novaLista2)

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
l.append(10)
l.append(20)
l.append(3)
l.append(4)
l.append(23)
l.append(20)

l.divideLista()



