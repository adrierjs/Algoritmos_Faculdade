class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []


class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []
        self.next = None


class MultiUni:
    def __init__(self):
        self.head = None

    def cadastrarUni(self, nome):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Universidade(nome)
        else:
            self.head = Universidade(nome)

    def buscarUni(self, nome):
        aux = self.head
        while aux and aux.nome != nome:
            aux = aux.next
        return aux

    def cadastrarDisciplina(self, nome, universidade):
        uni = self.buscarUni(universidade)
        if uni:
            uni.disciplinas.append(Disciplina(nome))
        else:
            print('Universidade Inexistente')

    def cadastrarAluno(self, nome, matricula, universidade, disciplina):
        uni = self.buscarUni(universidade)
        if uni:
            for disc in uni.disciplinas:
                if disc.nome == disciplina:
                    disc.alunos.append(Aluno(nome, matricula))
        else:
            print('Disciplina Inexistente')

    def print_dados(self):
        aux = self.head
        while aux:
            print(aux.nome)
            for disc in aux.disciplinas:
                print('    ', disc.nome)
                for aluno in disc.alunos:
                    print('                 ', aluno.nome, '-', aluno.matricula)

            aux = aux.next


multi = MultiUni()
multi.cadastrarUni('uepb')
multi.cadastrarUni('ufcg')
multi.cadastrarUni('ufc')
multi.cadastrarDisciplina('computação', 'uepb')
multi.cadastrarDisciplina('adm', 'uepb')
multi.cadastrarDisciplina('artes', 'ufc')
multi.cadastrarDisciplina('odonto', 'ufcg')
multi.cadastrarAluno('miguel', 1111, 'ufc', 'artes')
multi.cadastrarAluno('airton', 2222, 'ufc', 'artes')
multi.cadastrarAluno('luanda', 1558, 'uepb', 'computação')
multi.cadastrarAluno('talita', 6666, 'uepb', 'computação')
multi.cadastrarAluno('luiza', 8854, 'uepb', 'adm')
multi.cadastrarAluno('Natty', 2056, 'uepb', 'adm')
multi.cadastrarAluno('arthu', 7777, 'ufcg', 'odonto')
multi.cadastrarAluno('caio', 9999, 'ufcg', 'odonto')
multi.print_dados()