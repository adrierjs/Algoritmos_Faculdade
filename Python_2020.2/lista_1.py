# -*- coding: utf-8 -*-
"""lista 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L7FSzBuKrd7YZdLhDLNq1oI4lXM1ZD44

**Número 1**
"""

preco = float (input("Digite o valor do litro do combustível: "))
saldo = float (input("Digite o valor dísponivel para abastacimento: "))
resul =(saldo/preco)
print("o valor abastecido é:", resul, ("Litros"))

"""**Número 2**"""

kmi=float(input("Digite o KM inicial: " ))
kmf=float(input("Digite o KM final: " ))
lit=float(input("Digite quantos litros foram gastos: " ))
resul= kmf-kmi
valor= resul/lit
print("O valor médio gasto de combustível foi: ", valor, ("Litros"))

"""**Numero 3**"""

print("Olá, quer descobrir quanto ficará o valor de sua dívida em atraso contando os juros?")
valor=float(input("Digite o valor da sua dívida: "))
dia=int(input("Digite a quantidade de dias que a sua dia está atrasada: "))
juros=float(input("Digite o valor cobrado por dia de atraso: "))
resultado=(dia*juros)
final=(resultado+valor)
print("O valor final a ser pago é de: ", final)

"""**Número 4**

"""

print("Olá, vamos calcular a área total da sua casa? ")
l1=float(input("Digite a largura do primeiro cômodo: "))
c1=float(input("Digite o comprimentro do primeiro cômodo: "))
re1=(l1*c1)
print("A área total do primeiro cômodo é: ", re1, "M²")
l2=float(input("Digite a largura do segundo cômodo: "))
c2=float(input("Digite o comprimentro do segundo cômodo: "))
re2=(l2*c2)
print("A área total do segundo cômod é:", re2, "M²")
l3=float(input("Digite a largura do terceiro cômodo: "))
c3=float(input("Digite o comprimentro do terceiro cômodo: "))
re3=(l3*c3)
print("A área total do terceiro cômodo é de: ", re3, "M²")
l4=float(input("Digite a largura do quarto cômodo: "))
c4=float(input("Digite o comprimentro do quarto cômodo"))
re4=(l4*c4)
print("A área total do terceiro cômodo é de: ", re3, "M²")
total=(re1+re2+re3+re4)
print("A área total da sua casa é de:", total, "M²")

"""**Número 5**"""

print("Converção de dólar para real")
cot=float(input("Informe a cotação atual do dólar: "))
real=float(input("Informe quanto em real você deseja converter para o dólar: "))
resul=(real/cot)
print("O valor em dólares é: ", resul, "US$")

"""**Número 6**"""

print("Valor do seu salário após o reajuste")
salario=float(input("Insira o valor do seu salário: R$"))
per=float(input("Insira agora o percentual: %"))
ope=(salario*per/100)
resul=(ope+salario)
print("O valor do seu salário após o reajuste é de: R$", resul)

"""**Numero 7**"""

print("Olá, quer saber em quantos anos você terá 1 milhão de reais? Vamos prosseguir!")
salario=int (input("Digite o seu salário mensal: "))
despesas=int (input("Digite as suas despensas mensais: "))
bruto=(salario-despesas)
ano=(bruto*12)
resultado=(1000000/ano)
print("Você terá 1 milhão de reais em: ",resultado, "anos")

"""**Número 8**"""

nu=int(input("Insira um número: "))
n1=(nu-1)
n2=(nu-2)
n3=(nu+1)
n4=(nu+2)
print(n2, n1, nu, n3, n4)

"""**Número 9**

"""

nome=(input("Insira o seu nome: "))
idade=int(input("Insira o seu ano de nascimento: "))
ano=2021
final=(ano-idade)
print(nome, "tem", final, "anos")

"""**Número 10**

"""

largura=float(input("Digite o valor da largura: "))
comprimentro=float(input("Digite o valor do comprimentro:"))
cadeira=float(input("Digite o valor do comprimentro da cadeira:"))
larguratotal=(largura+0.5)/(cadeira+0.5)
compritotal=(comprimentro-1.5+0.2)/(cadeira+0.2)
totalcad=(larguratotal*compritotal)
print("A quantidade de cadeiras será:",int(totalcad), "na sala.")