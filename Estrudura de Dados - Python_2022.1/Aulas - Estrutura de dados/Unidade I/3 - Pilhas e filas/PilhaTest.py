class Pilha:
    def __init__(self):
        self.head = []

    def push(self, value):
        self.head.append(value)

    def pop(self):
        self.head.pop()

    def isEmpty(self):
        # return len(self.head) == 0
        if len(self.head) ==0:
            return self.head

    # def imprime(self):
    #     output = '('
    #     for i in range()


p = Pilha()
p.push(20)
print(p.head)



