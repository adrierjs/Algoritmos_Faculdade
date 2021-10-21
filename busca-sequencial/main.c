#include <stdio.h>
#include <locale.h>
int verificar(int vet[],int valor, int tam){
  int i;
  for (i=0;i<tam;i++){
	if (vet[]==valor){ /*comparação*/
    return 1;
   }
  }
return -1;
}
int main(void) {
  setlocale(0, "Portuguese");
  int vetor[10]={1,2,3,4,5,6,7,8,9,10};
/*               0 1 2 3 4 5 6 7 8 9   */
  int tam = 10;
  int valor, r, pos;
  printf("Digite um valor:\n ");
  scanf("%d", &valor);
  r = verificar(vetor, valor, tam); /*Chamada da função*/

if(r==1){
  printf("Valor %d encontrado!\n",valor);
} else {
  printf("Valor %d não encontrado!\n",valor);
}

  return 0;
}
