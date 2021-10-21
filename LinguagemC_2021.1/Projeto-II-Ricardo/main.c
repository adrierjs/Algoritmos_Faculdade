#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//menu
int menu(){
  printf(" 1 - Inserir novo contribuinte\n 2 - Informar próximo membro a contribuir;\n 3 - Imprimir lista completa;\n 0 - Sair\n");

return 0;
}
//menu
int ler_menu(){
  menu();
  int entrada = -1;

  while(entrada != 0){
    printf("Digite: ");
    scanf("%d", &entrada);
    switch(entrada){
      case 1:
      return entrada;
      case 2:
      return entrada;
      case 3:
      return entrada;
      case 0:
      break;
      default:
        printf("O valor foi inválido, digite novamente\n\n");
        menu();
    }
  }
  return 0;
}
//inicializar
typedef struct cliente{
  char nome[50];
  struct cliente *prox;
} cliente;

cliente* inicializar(){
  return NULL;
}
void inserir_inicio(cliente** lista, char nome[50]){
  cliente* novo = malloc(sizeof(cliente));
  strcpy(novo->nome,nome);
  if(*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  } else {
    novo->prox = *lista;
    *lista = novo;
  }
}

//no fim
void inserir_fim(cliente** lista, char nome[50]){
  cliente* novo = malloc(sizeof(cliente));
  strcpy(novo->nome,nome);
  if(*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  } else {
    cliente* p = *lista;
    while(p->prox!=NULL){
      p = p->prox;
    }
    p->prox = novo;
  }
}

void proximo_contribuir(cliente** lista){
  if(*lista !=NULL){
    printf("O contribuinte atual é: %s\n",(*lista)->nome);
    inserir_fim(lista,(*lista)->nome);
    cliente* aux = *lista;
    *lista = (*lista) ->prox;
    free(aux);
  }else{
    printf("Não a contribuintes cadastrados!\n");
  }
}

void imprimir(cliente* lista){
  printf("--Clientes--\n");
  while(lista != NULL){
    printf("Nome: %s\n",lista->nome);
    lista=lista->prox;
  }
}

int main(void) {
char novoCliente[50];
char cliente2[50];
int entrada = ler_menu();
cliente* lista = inicializar();

while(entrada != 0){


  if(entrada == 1){
    printf("Digite o nome do novo contribuinte: ");
    scanf("%s",novoCliente);
    inserir_fim(&lista,novoCliente);
    entrada = ler_menu();
  }

  else if(entrada ==2){
  proximo_contribuir(&lista);

    entrada = ler_menu();
  }else if(entrada ==3){
    imprimir(lista);
    entrada = ler_menu();
  }
}
return 0;
}