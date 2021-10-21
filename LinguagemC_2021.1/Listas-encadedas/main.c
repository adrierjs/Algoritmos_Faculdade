#include <stdio.h>
#include <stdlib.h>




typedef struct{
  int info;
  struct Lista *prox;
} Lista;

Lista * inserir (Lista *inicio, int i){
  inicio = (Lista *) malloc(sizeof(Lista));
  inicio -> info = i;
  inicio -> prox = NULL;
  return inicio;


}



int main(void) {
  Lista *inicio = NULL; //se nao tiver nada na lista, aponta para nulo;

if (inicio == NULL){//lista vazia

inicio = inserir(inicio, 100);
  printf("O valor é: %d", inicio->info);

}






  return 0;
}