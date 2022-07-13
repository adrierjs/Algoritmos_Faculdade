def calcularCarro(km, dias):
  if(dias != 0):
    resultado = (km * 0.15) + (dias * 60)
    return resultado
  else:
    print("Não existe 0 dias, tente novamente!")
    insereDados()

def insereDados():
  km = float(input("Quantos KM foram percorridos?"))
  dias = float(input("Quantos dias utilizou o carro?"))
  resultado = calcularCarro(km, dias)
  if(resultado):
    print("Você pagará:R$", resultado)