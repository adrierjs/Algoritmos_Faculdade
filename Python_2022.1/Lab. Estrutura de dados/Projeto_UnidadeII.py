class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.notas = [None, None]

    def addNota(self, nota):
        if not self.notas[0]:
            self.notas[0] = nota
        elif not self.notas[1]:
            self.notas[1] = nota
        else:
            print('Disciplina já possui duas notas.')

    def atualizarNota(self, notaNova, indiceNota):
        if indiceNota == 1:
            self.notas[0] = notaNova
        elif indiceNota == 2:
            self.notas[1] = notaNova
        else:
            print('Indice inválido.')

    def getMedia(self):
        if self.notas[0] and self.notas[1]:
            return (self.notas[0] + self.notas[1]) / 2
        else:
            return -1


class NoAluno:
    def __init__(self, nome):
        self.nome = nome
        self.left = None
        self.right = None
        self.disciplinas = []

    def addAluno(self, aluno):
        if aluno.nome > self.nome:
            if not self.right:
                self.right = aluno
            else:
                self.right.addAluno(aluno)
        else:
            if not self.left:
                self.left = aluno
            else:
                self.left.addAluno(aluno)

    def getAluno(self, nome):
        lista = []
        self.gerarLista(lista)
        for aluno in lista:
            if aluno.nome == nome:
                return aluno

    def addDisciplina(self, nomeAluno, nomeDisciplina):
        aluno = self.getAluno(nomeAluno)
        if aluno:
            dis = Disciplina(nomeDisciplina)
            aluno.disciplinas.append(dis)
        else:
            print('Aluno nao encontrado!')

    def updateAluno(self, nomeAluno, novoNomeAluno):
        aluno = self.getAluno(nomeAluno)
        if aluno:
            aluno.nome = novoNomeAluno
        else:
            print('Aluno nao encontrado!')

    def updateDisciplina(self, nomeAluno, nomeDisciplina, novoNomeDisciplina):
        aluno = self.getAluno(nomeAluno)
        if not aluno:
            print('Aluno nao existe')
        else:
            dis = aluno.getDisciplina(nomeDisciplina)
            if not dis:
                print('Esse aluno nao tem essa disciplina')
            else:
                dis.nome = novoNomeDisciplina

    def updateNota(self, nomeAluno, nomeDisciplina, indiceNota, novaNota):
        aluno = self.getAluno(nomeAluno)
        if not aluno:
            print('Aluno nao existe')
        else:
            dis = aluno.getDisciplina(nomeDisciplina)
            if not dis:
                print('Esse aluno nao tem essa disciplina')
            else:
                dis.atualizarNota(novaNota, indiceNota)

    def addNota(self, nomeAluno, nomeDisciplina, nota):
        aluno = self.getAluno(nomeAluno)
        if not aluno:
            print('Aluno nao existe')
        else:
            dis = aluno.getDisciplina(nomeDisciplina)
            if not dis:
                print('Esse aluno nao tem essa disciplina')
            else:
                dis.addNota(nota)

    def removeDisciplina(self, nomeAluno, nomeDisciplina):
        aluno = self.getAluno(nomeAluno)
        if aluno:
            for i in range(len(self.disciplinas)):
                if aluno.disciplinas[i].nome == nomeDisciplina:
                    aluno.disciplinas.pop(i)
        else:
            print('Aluno nao encontrado!')

    def getDisciplina(self, nome):
        for disciplina in self.disciplinas:
            if disciplina.nome == nome:
                return disciplina

    def imprimirDisciplinas(self):
        for disciplina in self.disciplinas:
            print(disciplina.nome, end=' ')

    def imprimirOrdemAlfabetica(self):
        lista = []
        self.gerarLista(lista)
        listaNomes = []
        for aluno in lista:
            listaNomes.append(aluno.nome)
        listaNomes.sort()
        for nome in listaNomes:
            print(nome)

    def gerarLista(self, lista):
        if self.nome:
            lista.append(self)
            if self.left:
                self.left.gerarLista(lista)
            if self.right:
                self.right.gerarLista(lista)

    def removerAluno(self, nomeAluno):
        lista = []
        self.gerarLista(lista)
        for i in range(len(lista)):
            lista[i].left = None
            lista[i].right = None
            if lista[i].nome != nomeAluno:
                if i == 0:
                    self = lista[i]
                else:
                    self.addAluno(lista[i])

    def imprimirMediaAluno(self, nomeAluno, nomeDisciplina):
        aluno = self.getAluno(nomeAluno)
        if not aluno:
            print('Aluno nao existe')
        else:
            dis = aluno.getDisciplina(nomeDisciplina)
            if not dis:
                print('Esse aluno nao tem essa disciplina')
            else:
                print('A média desse estudante é: ', dis.getMedia())

    def imprimirAlunosMediaBaixa(self):
        if self.left:
            self.left.imprimirAlunosMediaBaixa()
        if self.nome:
            for dis in self.disciplinas:
                if dis.getMedia() < 7:
                    print('Nome  : ', self.nome)
                    print('Media : ', dis.getMedia())
                    print()
        if self.right:
            self.right.imprimirAlunosMediaBaixa()

    def imprimirAlunosMediaAlta(self):
        if self.left:
            self.left.imprimirAlunosMediaAlta()
        if self.nome:
            for dis in self.disciplinas:
                if dis.getMedia() >= 7:
                    print('Nome  : ', self.nome)
                    print('Media : ', dis.getMedia())
                    print()
        if self.right:
            self.right.imprimirAlunosMediaAlta()

    def imprimirNotas(self, nomeAluno):
        aluno = self.getAluno(nomeAluno)
        if not aluno:
            print('Aluno nao existe')
        else:
            for dis in aluno.disciplinas:
                if dis.getMedia() >= 0:
                    print('Disciplina: ', dis.nome)
                    print('Media     : ', dis.getMedia())
                    print()


root = None

# Para Teste - APAGAR DEPOIS!!!!!!!!!!!!
root = NoAluno('Firmino')
root.addAluno(NoAluno('Adrier'))
root.addAluno(NoAluno('Vitora'))
root.addAluno(NoAluno('Davi'))
root.addAluno(NoAluno('Matheus'))
root.addAluno(NoAluno('Pedo'))

root.addDisciplina('Davi', 'Fisica')
root.addDisciplina('Adrier', 'Mat')
root.addNota('Adrier', 'Mat', 10)
root.addNota('Adrier', 'Mat', 7)
root.addNota('Davi', 'Fisica', 5)
root.addNota('Davi', 'Fisica', 7)
# -------------------------------------

entrada = -1
while entrada != 0:
    print("-=" * 20)
    print("       SISTEMA ESCOLAR        ")
    print('1 -  Cadastrar aluno ')
    print('2 -  Cadastrar disciplina em aluno ')
    print('3 -  Cadastrar nota em disciplina de aluno ')
    print('4 -  Remover aluno ')
    print('5 -  Remover disciplina de aluno ')
    print('6 -  Atualizar aluno ')
    print('7 -  Atualizar disciplina de aluno ')
    print('8 -  Atualizar nota de disciplina de aluno ')
    print('9 -  Visualizar a média do aluno em uma disciplina')
    print('10-  Visualizar os nomes dos alunos em ordem alfabética')
    print('11-  Visualizar os nomes dos alunos que estão com média menor que 7')
    print('12-  Visualizar os nomes dos alunos que estão com média maior ou igual a 7')
    print('13-  Visualizar as notas das disciplinas cadastradas em um aluno')
    print('0 -  Sair')
    entrada = int(input('Escolha uma opcao: '))
    print("-=" * 20)

    if entrada == 1:
        nome = input('Nome do novo aluno: ')
        if not root:
            root = NoAluno(nome)
        else:
            root.addAluno(NoAluno(nome))

    elif entrada == 2:
        nomeDisciplina = input('Digite o nome da disciplina: ')
        nomeAluno = input('Digite o nome do aluno que receberá a disciplina: ')
        root.addDisciplina(nomeAluno, nomeDisciplina)

    elif entrada == 3:
        nomeAluno = input('Digite o nome do aluno que receberá a nota: ')
        nomeDisciplina = input('Digite o nome da disciplina que receberá a nota: ')
        nota = float(input('Digite a nota: '))
        root.addNota(nomeAluno, nomeDisciplina, nota)

    elif entrada == 4:
        nomeAluno = input('Digite o nome do aluno para remover: ')
        root.removerAluno(nomeAluno)

    elif entrada == 5:
        nomeAluno = input('Digite o nome do aluno que terá a disciplina removida: ')
        nomeDisciplina = input('Digite o nome da disciplina a ser removida: ')
        root.removeDisciplina(nomeAluno, nomeDisciplina)

    elif entrada == 6:
        nomeAluno = input('Digite o nome do aluno que terá o nome atualizado: ')
        novoNomeAluno = input('Digite o novo nome: ')
        root.updateAluno(nomeAluno, novoNomeAluno)

    elif entrada == 7:
        nomeAluno = input('Digite o nome do aluno que terá a disciplina atualizada: ')
        nomeDisciplina = input('Digite o nome da disciplina que será atualizada: ')
        novoNomeDisciplina = input('Digite o novo nome da disciplina: ')
        root.updateDisciplina(nomeAluno, nomeDisciplina, novoNomeDisciplina)

    elif entrada == 8:
        nomeAluno = input('Digite o nome do aluno que terá a nota atualizada: ')
        nomeDisciplina = input('Digite o nome da disciplina que terá a nota atualizada: ')
        indiceNota = int(input('Digite qual nota será atualizada [1 ou 2]: '))
        novaNota = float(input('Digite a nova nota: '))
        root.updateNota(nomeAluno, nomeDisciplina, indiceNota, novaNota)

    elif entrada == 9:
        nomeAluno = input('Digite o nome do aluno: ')
        nomeDisciplina = input('Digite o nome da disciplina: ')
        root.imprimirMediaAluno(nomeAluno, nomeDisciplina)

    elif entrada == 10:
        root.imprimirOrdemAlfabetica()

    elif entrada == 11:
        root.imprimirAlunosMediaBaixa()

    elif entrada == 12:
        root.imprimirAlunosMediaAlta()

    elif entrada == 13:
        nomeAluno = input('Digite o nome do aluno: ')
        root.imprimirNotas(nomeAluno)

    elif entrada == 0:
        print('Saindo...')

    else:
        print('Opcao invalida')

    print()