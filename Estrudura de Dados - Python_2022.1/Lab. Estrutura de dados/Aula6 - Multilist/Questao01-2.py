
class Universidade:
    def __init__(self, universidade):
        self.universidade = universidade
        self.next = None
        self.disciplinas = None

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Disciplina:
    def __init__(self, disciplina):
        self.disciplina = disciplina
        self.next = None
        self.alunos = None

class Multilista:
    def __init__(self):
        self.head = None

    def cadastrarUniversidade(self, universidade):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Universidade(universidade)
        else:
            self.head = Universidade(universidade)

    def buscarUniversidade(self, universidade):
        aux = self.head
        while aux and (aux.universidade != universidade):
            aux = aux.next
        return aux

    def cadastrar_disciplina(self, universidade, disciplina):
        universidade = self.buscarUniversidade(universidade)
        if universidade.disciplinas:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.disciplina = Disciplina(disciplina)
        else:
            self.head = Disciplina(disciplina)

    def buscar_disciplina(self, universidade, disciplina):
        aux = self.head
        while aux and (aux.universidade != universidade and aux.disciplina != disciplina):
            aux = aux.next
        return aux

    def cadastrar_aluno(self, universidade, disciplina, aluno):
        disciplina = self.buscar_disciplina(universidade,disciplina)
        aux = self.head
        if aux:
            if aux.disciplina:
                while aux.next:
                    aux = aux.next
                aux.aluno = Aluno(aluno)
            else:
                self.head = Aluno(aluno)
        else:
            print('A disciplina não existe')

multi = Multilista()
multi.cadastrarUniversidade('uepb')
multi.cadastrar_disciplina('uepb','poo')
multi.cadastrar_aluno('uepb','lab','adrier')


