#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct aluno{
  char nome[50];
  char matricula[8];
  struct aluno *prox;
} Aluno;

Aluno* inicializar(){
  return NULL;
}
// passar a lista por referência
void inserir_inicio(Aluno** lista, char nome[50], char mat[8]){
  Aluno* novo = malloc(sizeof(Aluno));
  strcpy(novo->nome,nome);
  strcpy(novo->matricula,mat);
  if(*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  } else {
    novo->prox = *lista;
    *lista = novo;
  }
}

// passar lista por referência
void inserir_fim(Aluno** lista, char nome[50], char mat[8]){
  Aluno* novo = malloc(sizeof(Aluno));
  strcpy(novo->nome,nome);
  strcpy(novo->matricula,mat);
  if(*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  } else {
    Aluno* p = *lista;
    while(p->prox!=NULL){
      p = p->prox;
    }
    p->prox = novo;
  }
}

void imprimir(Aluno* lista){
  while(lista != NULL){
    printf("Matrícula: %s\n",lista->matricula);
    printf("Nome: %s\n",lista->nome);
    lista=lista->prox;
  }
}

void troca(int *a, int *b){
  int aux = *a;
  *a = *b;
  *b = aux;
}

void remover_inicio(Aluno** lista){
  if(*lista != NULL){
    Aluno* aux = *lista;
    *lista = (*lista)->prox;
    free(aux);
  }
}

int main(void) {
  //int x = 10;
  //int y = 20;
  //printf("%d, %d\n",x,y);
  //troca(&x,&y);
  //printf("%d, %d\n",x,y);
  Aluno* lista = inicializar();
  inserir_fim(&lista,"Ricardo", "1234");
  inserir_fim(&lista,"João", "1235");
  inserir_inicio(&lista,"Maria","1236");
  imprimir(lista);
  remover_inicio(&lista);
  printf("----------------\n");
  imprimir(lista);
  return 0;
}