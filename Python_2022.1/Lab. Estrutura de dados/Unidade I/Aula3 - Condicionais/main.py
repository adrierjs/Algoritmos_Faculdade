def menor_maior(num1, num2):

  if(num1 > num2):
    print("O número 1 é maior que o 2")

  elif(num1 < num2):
    print("O número 2 é maior que o número 1")

def igual_diferente(num1, num2):
  if(num1 == num2):
    print("O número 1 é igual ao número 2")
  elif(num1 != num2):
    print("O número 1 é diferente do número 2")

def maior_menorIgual(num1, num2):
  if(num1 >= num2):
    print("O número 1 é maior ou igual ao número 2")
  elif(num1 <= num2):
    print("O número 1 é menor ou igual ao número 2")

def calculaSegundos(d, h, m, s):
  resultado = s+(m*60)+(60*60)+(d+24*3600)
  return resultado

def imprimir(s, c):
  if c <len(s):
    print(s[c])
    imprimir(s,c+1)


imprimir("ADRIER",0)






#dias = int(input("Digite a quantidade de dias"))
#horas = int(input("Digite a quantidade de horas"))
#minutos = int(input("Digite a quantidade de minutos"))
#segundos = int(input("Digite a quantidade de segundos"))

#menor_maior(20,10)
#maior_menorIgual(20,21)
#print("Total de segundos: ",calculaSegundos(dias, horas, minutos, segundos))

#imprimir("Adrier",0)







