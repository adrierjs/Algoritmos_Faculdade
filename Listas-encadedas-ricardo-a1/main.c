#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct aluno{
  char nome[50];
  char matricula[8];
  struct aluno*prox; //Apontador para a próxima referência, ou seja, a próxima caixa.
} Aluno;

Aluno*inicializar(){ //função para retornar o NULL
  return NULL;
}

void inserir_inicio(Aluno *lista, char nome[50], char mat[8]){
 Aluno * novo =malloc(sizeof(Aluno)); //criei uma nova caixa
 strcpy(novo->nome,nome);//copiei do parâmento a string, por isso usei i strcpy. Após isso, entrei na nova caixa e coloquei o nome do aluno.
 strcpy(novo->matricula, mat); //copiei a matricula para dentro da caixa
 if (lista==NULL){ //SE A LISTA FOR NULA
 lista = novo; //a estrutura lista recebe a NOVA caixa
 lista->prox = NULL;//após a estrutuda lista receber a nova caixa, ela irá precisar apontar para um valor nulo, no caso o apontador (a seta) está na variável prox. A ESTRUTURA LISTA NA ULTIMA POSICÃO(NOVO), ENTRA NO PROX(SETINHA) E DEFINE A CAIXA NOVO COMO NULA;
} else{
  novo -> prox = lista; //entrei na caixa novo, peguei o prox(setinha) e atribui para a caixa lista;
  lista = novo; //a setinha agora vai para novo, ou seja novo passa a ser a primeira posição 

}

}
// para lista por referencia
void (inserir_fim(Aluno *lista, char nome[50], char mat[8])){
  Aluno * novo =malloc(sizeof(Aluno)); //criei uma nova caixa
 strcpy(novo->nome,nome);//copiei do parâmento a string, por isso usei i strcpy. Após isso, entrei na nova caixa e coloquei o nome do aluno.
 strcpy(novo->matricula, mat); //copiei a matricula para dentro da caixa
  if(lista == NULL){
  lista = novo; //a estrutura lista recebe a NOVA caixa
 lista->prox = NULL;

  } else{ 
    Aluno * p = lista; // o endereço P vai receber lista 
    while(p->prox!=NULL){//enquanto p(entrar na caixa) e ir para prox(setinha) for diferente de NULL, ele irá percorrer todas as posicões na caixa
      p = p -> prox; //p vai entrar na caixa e ir para o prox(->), tem que usar o P ao inves do lista, pois ele mesmo terá a posição dele mesmo;
    }
    p->prox = novo; //a caixa p recebe o novo valor
    novo->prox = NULL; //novo irá apontar para NULL, PARA ELE PARAR.
  }
}
void imprimir(Aluno * lista){
  while(lista!=NULL){
    //IMPRIME -> AVANÇA...
    printf("Matrícula: %s\n", lista->matricula); //entrei na caixa lista e peguei a matrícula
    printf("Nome: %szn",lista->nome);//entrei na caixa e peguei o nome
    lista = lista->prox;//avança na lista
  }
}

int main(void) {
  Aluno * lista = inicializar(); //O apontador agora virou a lista vazia, ou seja, sempre receberá o NULL;

  //pedir o nome e matrícula

  inserir_inicio(lista, nome, matricula); // para inserir um elemento na lista no inicio
  inserir_fim(lista, nome, matricula); //para inserir no fim da lista



  return 0;
}