# -*- coding: utf-8 -*-
"""Lista4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yKeATq8ofW_JmhdK0O49AaoOAooW6lzy

1) Implemente um programa que exiba a tabuada do 2 ao 9.
"""

for valor in range(2,10):
  for i in range(1,11):
    print(i,"X",valor,"=",i*valor,sep='') 
  print()

"""2) Faça um programa para tabular a função: f(x, y) = (x4 +3xy+y3 )/(2xy+3x+4y+2) para x = 2, 4, 6, 8 e y = 1, 3, 5, 7, 9, para cada valor de x. Devem ser impressos os valores de x, de y e de f(x,y).


"""

# Commented out IPython magic to ensure Python compatibility.
# %reset -f
for x  in range(2,9,2):
  for y in range(1,10,2):
    f=(x**4+3*x*y+y**3)/(2*x*y+3*x+4*y+2)
    print('f(',x,',',y,') = ',f, sep='')
  print()

ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 2 == 0:
            print(ch, ch, sep = '', end = '')
        else:
            print('  ', sep = '', end = '')
    print()

"""Questão 3

"""

ch = "*"
for linha in range(8):
    for coluna in range(8):
        if coluna:
            print(ch, ch, sep = '', end = '')
    print()

"""Questão 4"""

ch = "*"
for linha in range(8):
    for coluna in range(8):
        if coluna==linha or (linha+coluna==8-1):
            print(ch, ch, sep = '', end = '')
        else:
          print(" ",sep = "",end = "")
    print()

"""Questão 5"""

ch = "*"
for linha in range(8):
    for coluna in range(8):
        if coluna==linha or (linha+coluna==8-1):
            print(ch, ch, sep = '', end = '')
        else:
          print(" ",sep = "",end = "")
    print()

"""Questão 7

"""

ch = '*'
tam = 10
for linha in range(tam):
    for coluna in range(tam):
        if (linha <= coluna):
            print(ch, sep = '', end = '')
        else:
            print('', sep = '', end = '')
    print()