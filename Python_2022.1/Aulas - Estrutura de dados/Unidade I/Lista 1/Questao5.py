class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self,value):
        if(self.head):
            aux = self.head
            while (aux.next):
                aux = aux.next
            aux.next = Node(value)
        else:
            self.head = Node(value)
        self.__size +=1

    def __len__(self):
        return self.__size

    def __getitem__(self, index):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Elemento não encontrado')
            return aux.data
        else:
            raise IndexError('Lista vazia')

    def busca(lista, valor):
        tamanho = len(lista)
        inicio = 0
        final = tamanho - 1

        while True:
            meio = (inicio + final) // 2

            if inicio == final and valor != lista[meio]:
                return False

            if valor < lista[meio]:
                final = meio

            elif valor > lista[meio]:
                inicio = meio

                if inicio + 1 == final:
                    inicio = final

            else:
                return meio

    def retornaPosicao(self, value):
        if self.head:
            tam = self.__size
            retornoBusca = self.busca(value)

            if retornoBusca == 0 or retornoBusca != False:
                for i in range(tam):
                    if self[i] == value:
                        return i
            else:
                return False
        else:
            raise IndexError('Lista vazia')


l = LinkedList()
l.append(0)
l.append(4)
l.append(3)
print(l.retornaPosicao(0))



