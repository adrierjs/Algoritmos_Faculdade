#include <stdio.h>
#include <stdlib.h>

struct Aluno{ //estrutura
  int matricula;
  char nome[10];
};


int main(void) {
  printf("Estrutuas(registros)\n");

 struct Aluno lista[2];

 int i;
 int tam = 2;
 for(i=0;i<2;i++){
    printf("Insira a matricula e o nome do aluno %d\n",i+1);
    scanf("%d",&lista[i].matricula);
    fflush(stdin);
    fgets(lista[i].nome, sizeof(lista[i].nome, stdin);

 }
  for(i=0;i<2;i++){

    printf("A matricula do aluno %s eh %d\n",lista[i].nome,lista[i].matricula);

 }
  return 0;
}