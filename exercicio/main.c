#include <stdio.h>
#include <string.h>

int main(void){
  char nome[10];
  int v;
  char sobrenome[10]= "oliveira";
  printf("Digite seu nome: ");
  scanf("%s",nome);
  v= strcmp(nome, sobrenome);
  printf("%d\n",v);
  

	


return(0);
}




//insira o seu código
