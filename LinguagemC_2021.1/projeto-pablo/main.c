#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct cliente{
  char nome[40];
  char telefone[15];
  char celular[15];
  char email[40];
  struct cliente *prox;
} cria_agenda;

void menu(){
printf("---------------------------------\n");
printf("        AGENDA DE CONTATOS       \n");
printf("---------------------------------\n\n");
printf("1 – Inserir o contato na primeira posição da agenda:\n");
printf("2 – Listar contatos\n"); 
printf("3 – Buscar contato\n"); 
printf("4 - Excluir o contato na primeira posição da agenda:\n");
printf("5 - Excluir Agenda\n");
printf("6 – Sair\n\n");  
};

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
      case 4:
      return entrada;
      case 5:
      return entrada;
      case 6:
      return entrada;
      default:
        printf("O valor foi inválido, digite novamente\n\n");
        menu();
    }
  }
  return 0;
}


//inicializar agenda
cria_agenda* inicializar(){
  return NULL;
}


void inserir_inicio(cria_agenda** lista, char nome[50], char telefone[15], char celular[15], char email[40]){
  cria_agenda* novo = malloc(sizeof(cria_agenda));
  strcpy(novo->nome,nome);
  strcpy(novo->telefone,telefone);
  strcpy(novo->celular,celular);
  strcpy(novo->email,email);
  if(*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  } else {
    novo->prox = *lista;
    *lista = novo;
  }
}

void lista_contatos(cria_agenda* lista){
  
 
  printf("--Contatos--\n");
  if(lista == NULL){
    printf("Não há contatos na lista!\n");
  }
  while(lista != NULL){
    printf("Nome: %s\n",lista->nome);
    printf("Telefone: %s\n",lista->telefone);
    printf("Celular: %s\n",lista->celular);
    printf("Email: %s\n",lista->email);
    lista=lista->prox;
    printf("\n");
  } 
}

void remover_inicio(cria_agenda** lista){
  if(*lista != NULL){
    cria_agenda* aux = *lista;
    *lista = (*lista)->prox;
    free(aux);
  }
}

void excluir_agenda(cria_agenda** lista){
  while(*lista != NULL){
    cria_agenda* aux = *lista;
    *lista = (*lista)->prox;
    free(aux);
  }
}
//-----------------------------------------------------

int main(void) {

  char novo_nome[50];
  char novo_telefone[50];
  char novo_celular[50];
  char novo_email[50];
  int entrada = ler_menu();
  cria_agenda* lista = inicializar();

while(entrada != 0){


  if(entrada == 1){
    printf("Digite o nome: ");
    scanf("%s",novo_nome);
    printf("Digite o telefone: ");
    scanf("%s",novo_telefone);
    printf("Digite o celular: ");
    scanf("%s",novo_celular);
    printf("Digite o email: ");
    scanf("%s",novo_email);
    inserir_inicio(&lista, novo_nome,novo_telefone,novo_celular,novo_email);
    
    entrada = ler_menu();
  
  }else if(entrada ==2){
    lista_contatos(lista);
    entrada = ler_menu();
  }else if(entrada ==3){
    entrada = ler_menu();
  }
  
  else if(entrada ==4){
    remover_inicio(&lista);
     entrada = ler_menu();
  } else if(entrada ==5){
    excluir_agenda(&lista);
    printf("Agenda excluída!\n");
    entrada = ler_menu();
  } 
  
  /*else if(entrada ==6){
    if (lista != NULL){
      FILE *doc;
      doc = fopen("contatos.txt","wt");
      while ( lista != NULL){
        char contato[250];
        sprintf(contato,"Nome:%s, telefone:%s, celular:%s, email:%s",lista->nome,lista->telefone,lista->celular,lista->email);
        fputs(contato, doc);
      }
      fclose(doc);
    }*/

    break;
  
}
return 0;
}



