#def imprimir(s, c):
  #if c <len(s):
    #print(s[c])
    #imprimir(s,c+1)
from importlib.metadata import entry_points


def inserir(lista, tam):
  if tam < 4:
    dado = input("digite o dado")
    lista.append(dado)
    inserir(lista, tam+1)

tam = 0
lista = []*4
inserir(lista,tam)
print(lista)





