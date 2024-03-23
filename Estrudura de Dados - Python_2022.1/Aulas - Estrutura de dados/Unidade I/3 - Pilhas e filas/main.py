class Stack:
  def __init__(self):
    self.head = []

  def push(self,value):
    self.head.append(value)

  def pop(self):
     return self.head.pop()

  def isEmpty(self):
    return len(self.head) == 0

def verifique_parentesis(expressao):
  pilha = Stack()
  for i in expressao:
    if i == '(':
      pilha.push(i)
    elif i == ')':
      if pilha.isEmpty():
        return False
      pilha.pop()

  return pilha.isEmpty()

expressao = '(()))'

print(verifique_parentesis(expressao))
