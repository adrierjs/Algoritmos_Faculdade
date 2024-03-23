class Disciplina:
    def __init__(self,nome):
        self.nome = nome
        self.notas = [0]*2

    def addNota(self, nota):
        if self.notas[0] == 0:
            self.notas[0] = nota
        elif self.nota[1] == 0:
            self.notas[1] = nota
        else:
            print('As notas já foram cadastradas')


