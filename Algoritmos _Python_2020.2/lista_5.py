# -*- coding: utf-8 -*-
"""Lista 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZO5oqMu-iRNaD-90kPlqFJ2v1V1MpLbO

Exemplo do resumo
"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
lista = []
valor = int(input("Insira um número, e zero para encerrar: "))
while valor !=0:
  lista.append(valor)
  valor = int(input("Insira um número, e zero para encerrar: "))
print(lista)
remover = int (input("Digite um valor para ser removido da lista:"))
while remover in lista:
  lista.remove(remover)
print(lista)

"""Questão 1"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
a = [1,0,5,-2,-5,7]
print(a[0],a[1],a[5])
a[4] = 100
soma = a[0]+a[1]+a[5]
print(soma)
for i in(a):
  print(i)

"""Questão 2"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
lista = []
for i in range(10):
  valor = float(input("Digite um valor: "))
  lista.append(valor)#pega o valor digitiado e acrescenta na lista
print(lista)
nova_lista = []
for i in range(len(lista)):#faz o range de tudo que está na lista
  nova_lista.append(lista.pop(0)**2)#leu a nova lista e removeu o valor e colocou o novo (elevado a 2) no lugar do antigo
print(nova_lista)

"""Questão 3


"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
valores = 0
soma = 0
somarimpar = 0
for i in range(10):
  valores = int (input("Digite um valor: "))
  if valores % 2 ==0:
    soma+=1
    pares = [0]*soma
    for j in range(soma):
      pares[j] = valores
  else:
    somarimpar+=1
    impares = [0]*somarimpar
    for k in range(somarimpar):
      impares[k] = valores
    

    
print(pares,"são números são pares.",soma,'foi o total de pares.')

"""Questão 4"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
lista = [0]*10
for i in range(10):
  lista[i] = int (input('digite um número: '))
  maior = int (max(lista))
  posicao = lista.index(maior)
print('o número maior', maior)
print('a posição do maior número: ',posicao)

"""Questão 5"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
print('Gabarito')
nQuestoes = 3
gabarito = [0] *nQuestoes
for i in range(nQuestoes):
  print('Questão',i+1)
  gabarito[i] = input()

nAlunos = int(input('Quantos alunos há na turma? '))
for aluno in range(nAlunos):
  respostas = [0] *nQuestoes
  print('Aluno',aluno+1)
  for questao in range(nQuestoes):
    print('Resposta da Questão',questao+1)
    respostas[questao] = input()
  cont = 0
  for questao in range(nQuestoes):
    if gabarito[questao] == respostas[questao]:
      cont = cont + 1
  
  if cont == 1:
    print('O aluno',aluno+1,'acertou',cont,'questões')
  else: 
    print('O aluno',aluno+1,'acertou',cont,'questões.')

"""Questão 6"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
lista = []
nova_lista = []
for i in range(10):
  dig = int (input("Digite um valor: "))
  lista.append(dig)
  nova_lista.append(dig)
nova_lista.reverse()
print('numeros normais:',lista)
print('números invertidos:',nova_lista)

"""Questão 7"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f 
numeros = [20,20,21,22,23,10,10,12,34,53,64,23,12,32,34,67,87,54,19,20]
numeros2 = [1,2,3,4,5,6,7,8,9,0,2,12,32,45,64,75,34,654,21,20]
soma = numeros+numeros2
repetidos = []
diferenca = []
somavet = []
multiplicacao = []
for i in soma:
  if i not in diferenca:
    diferenca.append(i)
somavet = sum(soma)
print(diferenca)
print(somavet)

"""Questão 8"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
tam1 = int(input("Digite o tamanho da lista: "))
valor1 = [0]*tam1
valor2 = [0]*tam1
nova_lista = []
soma = 0
for i in range(tam1):
  valor1[i] = input("Digite o conteúdo da lista 1: ")
  valor2[i] = input("Digite o conteúdo da lista 2: ")
total = valor1+valor2
elementos = input("Digite quais elementos são repetidos: ")

print('o conteúdo da lista sem ocorrências',total)

"""Questão 9"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
valores = []
pares = []
impares = []
vezes = int (input("Digite quantos números você irá digitar: "))
for i in range(vezes):
  usuario = int (input("Digite um valor e -1 para finalizar: "))
  valores.append(usuario)
  if usuario % 2 ==0:
    pares.append(usuario)
  else:
    impares.append(usuario)
print(pares,"são pares.",impares, 'são ímpares')

"""Questão 10 """

# Commented out IPython magic to ensure Python compatibility.
# %reset -f 
numeros = []
repetidos = []
arquivo = []
usuario = []
for i in range(10):
  digitado = int(input('Digite um número: '))
  usuario.append(digitado)
numeros = usuario
for i in numeros:
  if i not in arquivo:
    arquivo.append(i)
  else:
    repetidos.append(i)
print(repetidos)