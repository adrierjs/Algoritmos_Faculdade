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

    def buscarAluno(self, nome, curso):
        aux = self.head
        while aux and (aux.nome != aux.nome or aux.turno !=aux.turno):
            aux = aux.next
        return aux

uepb = Multilista()
uepb.cadastrarCurso('Adrier', 'diurno')
print(uepb.buscarAluno('Adrier','diurno'))
