class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Universidade:
    def __init__(self, universidade):
        self.universidade = universidade
        self.disciplinas = []
        self.next = None

class Disciplina:
    def __init__(self, disciplina):
        self.disciplina = disciplina
        self.alunos = []

class MultiLista:
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

    def CadastrarDisciplina(self, universidade, disciplina):
        buscarUni= self.buscarUniversidade(universidade)
        if buscarUni:
            buscarUni.disciplinas.append(Disciplina(disciplina))
        else:
            print('A universidade não existe')

    def cadastrarAluno(self, nome, universidade, disciplina):
        uni = self.buscarUniversidade(universidade)
        if uni:
            for disciplina in uni.disciplinas:
                if disciplina.disciplina == disciplina:
                    disciplina.alunos.append(Aluno(nome))
        else:
            print('Disciplina Inexistente')

    def imprime(self):
        aux = self.head
        while aux:
            print(aux.universidade)
            for disciplina in aux.disciplinas:
                print(' ', disciplina.disciplina)
                for aluno in disciplina.alunos:
                    print(' ', aluno.nome, '-', aluno.matricula)
            aux = aux.next

multi = MultiLista()
multi.cadastrarUniversidade('uepb')
multi.CadastrarDisciplina('uepb', 'lab')
multi.cadastrarAluno('Adrier','uepb','lab')
multi.imprime()