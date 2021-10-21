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
printf("1 – Inserir o contato\n");
printf("2 – Listar contatos\n"); 
printf("3 – Buscar contato\n"); 
printf("4 - Excluir o contato\n");
printf("5 - Excluir Agenda\n");
printf("6 – Sair\n\n");  
};


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
    cria_agenda* tmp = *lista;
    if(nome[0]<(tmp->nome)[0]){
      novo->prox = *lista;
      *lista = novo;
    }
    else{
      while(tmp->prox != NULL && nome[0]>((tmp->prox)->nome)[0]){
          tmp = tmp->prox;
      }
         novo->prox = tmp-> prox;
         tmp->prox = novo;
    }
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
cria_agenda* busca_contato(cria_agenda* lista, char busca[40]){
  while(lista != NULL){   
    if(strcmp(lista->nome,busca)==0){
        return lista;
    }
    lista = (lista)->prox;
  }
  return NULL;
};

void exclui_contato(cria_agenda** lista, char busca[40]){    
    while(strcmp((*lista)->nome, busca)!=0){
        lista = &(*lista)->prox;
    }
    if(*lista == NULL){
      printf("Não existe contato com esse nome.");
    } 
    else{
      cria_agenda *tmp = *lista;
      *lista = (*lista)->prox;
      free(tmp);
      
    }
}

//-----------------------------------------------------

int main(void) {
    char novo_nome[40];
    char novo_telefone[15];
    char novo_celular[15];
    char novo_email[40];
    char busca[40];
    int entrada = -1;
    cria_agenda* lista = inicializar();

while(entrada != 0){
    menu();
    printf("Digite: ");
    scanf("%d", &entrada);      
    switch(entrada){
    case 1:
      printf("Digite o nome: ");
      scanf("%s",novo_nome);
      printf("Digite o telefone: ");
      scanf("%s",novo_telefone);
      printf("Digite o celular: ");
      scanf("%s",novo_celular);
      printf("Digite o email: ");
      scanf("%s",novo_email);
      inserir_inicio(&lista, novo_nome,novo_telefone,novo_celular,novo_email);
    break;
    
    case 2:
      lista_contatos(lista);
    break;

    case 3:
        printf("Qual contato você deseja buscar:");
        scanf("%s",busca);
        cria_agenda* Novocontato = busca_contato(lista,busca); 
        if(Novocontato != NULL){
        printf(" Contato encontrado!\n Nome:%s\n Telefone:%s\n Celular:%s\n Email:%s\n",Novocontato->nome,Novocontato->telefone,Novocontato->celular,Novocontato->email );
        }else{
            printf("Nome não encontrado\n");
        }
        break;
    
    case 4:
        printf("Qual contato você deseja excluir:");
        scanf("%s",busca);
        if(Novocontato != NULL){
            exclui_contato(&lista,busca);
        }else{
            printf("Contato não encontrado!\n");
        }
        break;
    
    case 5:
        excluir_agenda(&lista);
        printf("Agenda excluída!\n");
        break;
    
    case 6:
        if (lista != NULL){
        FILE *doc;
        doc = fopen("contatos.txt","wt");
        while ( lista != NULL){
            char contato[250];
            sprintf(contato,"Nome:%s, telefone:%s, celular:%s, email:%s\n",lista->nome,lista->telefone,lista->celular,lista->email);
            fputs(contato, doc);
            lista=lista->prox;
        }
        fclose(doc);
        }
        printf("Saindo do programa\n");
        entrada = 0;
        break;

    default:
      printf("O valor foi inválido, digite novamente\n\n");
      menu();
  }
}

return 0;
}
