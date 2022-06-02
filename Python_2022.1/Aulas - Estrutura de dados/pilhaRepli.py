class Stack:
    def __init__(self):
        self.head = []

    def push(self, value):
        self.head.append(value)

    def pop(self):
        return self.head.pop()

    def isEmpty(self):
        return len(self.head) ==0

    def imprimir(self):
        output = '('
        for i in range(len(self.head)):
            output += str(self.head[i])
            if i != (len(self.head)-1):
                output += '\n '
        output += ')'
        return output




p = Stack()
p.push(2)
p.push(4)
p.push(5)
p.push(10)
print(p.imprimir())


