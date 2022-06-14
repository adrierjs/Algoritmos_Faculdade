class Aluno:
  def __init__(self, nome, endereco):
    self.nome = nome
    self.endereco = endereco


class Curso:
  def __init__(self, nome, turno):
    self.nome = nome
    self.turno = turno
    self.alunos = []
    self.next = None

class Multilista:
    def __init__(self):
        self.head = None

    def cadastrarCurso(self, nome, turno):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Curso(nome, turno)
        else:
            self.head = Curso(nome, turno)

    def buscarCurso(self, nome, turno):
        aux = self.head
        while aux and (aux.nome != nome or aux.turno != turno):
            aux = aux.next
        return aux

    def cadastrarAluno(self, nome, endereco, nomeCurso, turnoCurso):
        curso = self.buscarCurso(nomeCurso, turnoCurso)
        if curso:
            curso.alunos.append(Aluno(nome, endereco))
        else:
            print('Curso inexistente.')

lista = Multilista()
lista.cadastrarCurso('Computacao','Diurno')
lista.cadastrarAluno('Adrier', 'js', 'Computacao', 'Diurno')



