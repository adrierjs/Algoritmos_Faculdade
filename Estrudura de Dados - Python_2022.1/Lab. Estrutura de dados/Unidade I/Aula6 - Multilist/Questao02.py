class Livro:
    def __init__(self,titulo):
        self.titulo = titulo

class Alunos:
    def __init__(self,nome):
        self.nome = nome
        self.livros = []
        self.next = None

class Multilista:
    def __init__(self):
        self.head = None

    def cadastrarAluno(self,nome):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Alunos(nome)

        else:
            self.head = Alunos(nome)

    def buscarAluno(self,nome):
        aux = self.head
        while aux and (aux.nome != nome):
            aux = aux.next
        return aux

    def cadastrarLivro(self,nome,livro):
        aluno = self.buscarAluno(nome)
        if aluno:
            aluno.livros.append(Livro(livro))
        else:
            print('O aluno não existe')

    def relatorio(self):
        aux = self.head
        while (aux):
            print('Aluno: {}'.format(aux.nome))
            for livro in aux.livros:
                print('Livro: {}'.format(livro.titulo))
            aux = aux.next

        print('---------')

    def removerAluno(self, nome):
        if self.head:
            aux = self.head
            if aux.nome == nome:
              self.head = aux.next
              del aux
            else:
              while aux and (aux.nome != nome):
                  ant = aux
                  aux = aux.next
              ant.next = None
              del aux
        else:
            print("Não há nenhum aluno cadastrado no sistema ainda!")

    def removerLivro(self,nome,titulo):
        if self.head:
            aluno = self.buscarAluno(nome)
            if aluno:
                for livro in aluno.livros:
                    if livro.titulo == titulo:
                        aluno.livros.remove(livro)
                    else:
                        print('O livro não existe')
            else:
                print('Não há nenhum aluno cadastrado')


biblioteca = Multilista()
biblioteca.cadastrarAluno('Adrier')
biblioteca.cadastrarLivro('Adrier','Python')
biblioteca.cadastrarAluno('José')
biblioteca.cadastrarLivro('José','Pequeno principe')
biblioteca.relatorio()
biblioteca.removerLivro('Adrier','Python')
biblioteca.relatorio()



