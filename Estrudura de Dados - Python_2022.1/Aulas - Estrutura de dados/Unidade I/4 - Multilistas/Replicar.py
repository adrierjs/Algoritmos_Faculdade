class Aluno:
    def __init__(self, nome, endereco):
        self.endereco = endereco
        self.nome = nome

class Curso:
    def __init__(self, nome_curso, turno):
        self.nome_curso = nome_curso
        self.turno = turno
        self.alunos = []
        self.next = None

class Multilist:
    def __init__(self):
        self.head = None


    def CadastrarCurso(self, nome_curso, turno):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Curso(nome_curso, turno)

        else:
            self.head = Curso(nome_curso, turno)


    def BuscarCurso(self, nome_curso, turno):
        aux = self.head
        while aux and (aux.nome_curso != nome_curso or aux.turno != turno):
            aux = aux.next
        return aux

    def CadastrarAlunos(self, nome_curso, turno, nome, endereco):
        curso = self.BuscarCurso(nome_curso, turno)
        if curso:
            curso.alunos.append(Aluno(nome, endereco))
        else:
            raise IndexError('O curso não esta cadastrado')

uepb = Multilist()
uepb.CadastrarCurso('Computacao', 'm')

uepb.CadastrarAlunos('Computacao','m','adrier', 'jose')