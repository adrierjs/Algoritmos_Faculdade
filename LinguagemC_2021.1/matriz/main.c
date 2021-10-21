#include <stdio.h>

int main(void) {
  int i, j, ordem;
  printf("Digite a ordem da matríz: ");
  scanf("%d",&ordem);
  int mat[ordem][ordem];
  for(i=0;i<ordem;i++){
    for(j=0;j<ordem;j++){
      printf("Matriz [%d][%d]:\n",i+1,j+1);
      scanf("%d",&mat[i][j]);
    } 
  }
  for(i=0;i<ordem;i++){ /* imprimir matriz */
    for(j=0;j<ordem;j++){
      printf("[%d]",mat[i][j]);
    }
  printf("\n");
  }
    
  return 0;
   }