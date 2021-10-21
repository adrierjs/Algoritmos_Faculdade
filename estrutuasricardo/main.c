mk

//ou definidir logo na estrutura.

typedef struct Aluno{ //estrutura definida ja com typedef, ou seja Aluno, será renomeado para Aluno, assim dispensando o uso de struct a todo momomento.
  int matricula;
  char nome[20];
} Aluno; //renomeação

typedef struct Dados{
  int telefone;
  char endereco[50];
  char disciplina[20];

}Dados;


int main(void) {
  int tam = 2;
  Aluno alunos[tam];
  Dados dados[tam];


  int i;

  for(i=0;i<tam;i++){
    printf("Digite o nome aluno %d:\n",i+1);
    setbuf(stdin, NULL); //limpar o lixo da memória
    fgets(alunos[i].nome, sizeof(alunos[i].nome), stdin);
    printf("Digite a matrícula do aluno %d:\n",i+1);
    scanf("%d",&alunos[i].matricula);

  }
  for(i=0;i<tam;i++){
    printf("Dados de %s",alunos[i].nome);
    printf("Telefone:\n");

    scanf("%d",&dados[i].telefone);
    printf("Endereço:\n");

    setbuf(stdin, NULL);
    fgets(dados[i].endereco,sizeof(dados[i].endereco),stdin);
    printf("Digite qual disciplina %scursa:",alunos[i].nome);
    fgets(dados[i].disciplina, sizeof(dados[i].disciplina),stdin);
    setbuf(stdin, NULL);
  }

  for(i=0;i<tam;i++){
    printf("\n");
    printf("Aluno:%sMatrícula:%d\nDisciplina:%sEndereço:%sTelefone: %d\n",alunos[i].nome,alunos[i].matricula,dados[i].disciplina, dados[i].endereco, dados[i].telefone);
  }

  return 0;
}