class Pilha:
    def __init__(self):
        self.head = []

    def push(self, value):
        self.head.append(value)

    def pop(self):
       return self.head.pop()

pilha = Pilha()
palavrainvert = ''
palavra = input("Digite a palavra")
for i in range(len(palavra)):
    pilha.push(palavra[i])

for i in range(len(palavra)):
    palavrainvert += (pilha.pop())

print(palavrainvert)







