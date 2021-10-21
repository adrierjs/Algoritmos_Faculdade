#include <stdio.h>

 void ler_vet(int vet[],int tam, int ultimo){
   int i;
   for(i=0;i<tam;i++){
     printf("Digite o %d valor ",i+1);
     scanf("%d",&vet[i]);
     }
  }

void imprimir(int vet[],int tam){
  int i;
  for(i=0;i<tam;i++){
    printf("%d ",vet[i]);
  }
}

void ordena_vet(int vet[], int tam){
  int i, j, aux;
for (j=0;j<tam;j++){
	for (i=0;i<tam;i++){
	if(vet[i]>vet[i+1]){
		aux=vet[i];
		vet[i]=vet[i+1];
		vet[i+1]=aux;
	}
}
}
}
int PesquisaBinaria (int vet[], int valor, int tam) {
     int inf = 0;     // limite inferior 
     int sup = tam-1; // limite superior 
     int meio;
     
     while (inf <= sup) {
          meio = (inf + sup)/2;
          if (valor == vet[meio]){
               return meio; 
			   }else
          if (valor < vet[meio]){
               sup = meio-1;
           }
          else{
               inf = meio+1;
           }
     }
     return -1;   // não encontrado
}
int main(void) {
  int tam = 10;
  int tam2 = (tam-1); // para ordenar o vetor, tenho que fazer tamanho -1
  int i, j, aux, ultimo;
  int vet[tam];
  ler_vet(vet,tam,ultimo);
  printf("Digite o último valor: ");
     scanf("%d",&ultimo);
    
//funções:
ordena_vet(vet,tam2);
ultimo = PesquisaBinaria(vet,ultimo,tam);

imprimir(vet,tam);
printf("\n");
if(ultimo ==-1){
  printf("O último valor digitado NÃO está no vetor!");
}
else{
  printf("O último valor digitado ESTÁ no vetor!");
}

  return 0;
}