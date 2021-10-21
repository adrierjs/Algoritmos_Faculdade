#include <stdio.h>

int PesquisaBinaria(int vetor[],int inicio,int fim,int valor){

  int meio=(inicio+fim)/2;
  if(inicio>fim){
    return -1;
  }
  if(vetor[meio]==valor){
    return meio;
  }
  else if(valor<vetor[meio]){
    return PesquisaBinaria(vetor,inicio,meio-1,valor);
  }
  else{
    return PesquisaBinaria(vetor,meio+1,fim,valor);
  }

}

 void ler_vet(int vet[],int tam){
   int i;
   for(i=0;i<tam;i++){
     printf("Digite o %d valor: ",i+1);
     scanf("%d",&vet[i]);
     }
  }
int imprime(int vet[], int tam){
  if(tam == 0){
    return 0;
  } else{
    return imprime(vet,tam-1), printf("%d,",vet[tam-1]);
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
printf("Os dados foram ordenados!\n");
}

int menu(){
  printf(" 1 - Inserir dados; \n 2 - Ordenar dados; \n 3 - Imprimir dados; \n 4 - Realizar busca; \n 0 - Sair. \n");

return 0;
}

int ler_menu(){
  int entrada;
  int neutro= -1;
  while(neutro == -1){
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
      case 0:
      return entrada;

      default:
        printf("O valor foi inválido, digite novamente\n\n");
        menu();

    }

  }
  return 0;

}

int main(void) {
   int valor, r, vetor,vet2;
   int entrada = -1;
   int tam = 3;
   int vet[tam];

while (entrada !=0){
  menu();
  entrada = ler_menu();

    if (entrada == 1){
      printf("Digite o tamanho do vetor:");
      scanf("%d",&tam);
      ler_vet(vet,tam);
      
    }
    
    else if (entrada == 2){
    ordena_vet(vet,tam-1);
    }


     else if (entrada == 3){
    imprime(vet,tam);
    printf("\n");

    }
    
   else if (entrada== 4){
    printf("Digite um valor para buscar:");
    scanf("%d",&valor);
    r = PesquisaBinaria(vet,0,tam-1,valor);
    if(r !=-1){
      printf("O valor foi entrado na posição: %d", r);
      printf("\n");
    }
    else{
      printf("Valor não encontrado!");
    }
    }
    else{
      printf("Programa encerrado");
    }
}
 return 0;
}