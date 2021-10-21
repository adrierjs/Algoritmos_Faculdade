#include <stdio.h>

int main(void) {
  int i, tam;
  printf("Digite quantos números:\n");
  scanf("%d",&tam);
  int vetor[tam];
  
  for(i=0;i<tam;i++){
    printf("Digite %d número:\n",i+1);
    scanf("%d",&vetor[i]);
    
  }
  
  printf("Números armazenados\n");
  for(i=0;i<tam;i++){
    printf("%d\n",vetor[i]);



  
  }
  return 0;
}