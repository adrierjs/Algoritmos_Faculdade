#include <stdio.h>


int PesquisaBinaria (int vet[], int valor, int tam){
     int ini = 0;     // limite inicial (o primeiro índice de vetor em C é zero          )
     int fim = tam-1; // limite final (termina em um número a menos. 0 a 9 são 10 números)
     int meio;
     
     while (ini <= fim){
          meio = (ini + fim)/2;// inicio+fim\2
          if (valor == vet[meio]){
               return meio;
			   }else
          if (valor < vet[meio]){ /*valor menor que o vetor na posição meio*/
           /*{1,2,3,4,5,6,7,8,9,10}
              0 1 2 3 4 5 6 7 8 9
           */
               fim = meio-1; 
           }
          else{ /*valor maior que vetor na posição meio*/
          /*{1,2,3,4,5,6,7,8,9,10}
             0 1 2 3 4 5 6 7 8 9
           */
               ini = meio+1;
           }
     }
     return -1;   // não encontrado
}
int main( )
{
printf("Busca binária\n");

int numeros[10]={1,2,3,4,5,6,7,8,9,10};
int i, valor, s;
int tam = 10;
printf("Qual é o valor a procurar?");
scanf("%d", &valor);

int e;
e = PesquisaBinaria (numeros, valor, tam);

if (e != -1){
	printf("Achou na posicao %d!", e);
}
else{
  printf("Valor não encontrado!");
}


return(0);
}