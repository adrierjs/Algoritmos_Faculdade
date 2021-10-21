#include <stdio.h>

 void ler_vet(int vet[],int tam){
   int a, b,i ;
   for(i=0;i<tam;i++){
     scanf("%d",&vet[i]);
   }
}
void imprimir(int vet[],int tam){
  int i;
  for(i=0;i<tam;i++){
    printf("%d ",vet[i]);
  }
}

int main(void) {
  int tam = 3;
  int vet[tam];
  ler_vet(vet,tam);
  imprimir(vet,tam);
  return 0;
}