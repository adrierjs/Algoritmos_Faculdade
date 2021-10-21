#include <stdio.h>
#include <stdlib.h>//funções rand 
#include <time.h>

int main(void) {
  int usuario, aleatorio;
  srand(time(NULL));
  aleatorio = rand()%100;//rad coloca número aleatorio
  printf("%d\n",aleatorio);
  usuario = -1;

do{
  printf("Digite um número e 0 para encerrar:\n");
  scanf("%d",&usuario);
}while((aleatorio != usuario)&&(usuario!=0) );

if (aleatorio == usuario){
  printf("Parabéns! Você acertou");
}
else{
  printf("Encerrado!");
}

  return 0;
}