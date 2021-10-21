#include <stdio.h>
#include <stdlib.h> // as funções são dessa biblioteca
/*
malloc - para reservar memória
calloc
realloc - para aumentar memória
free - libera o espaço de memória utilizado*/
int main(void) {
 int *p;
 int i, t;


 p = (int*)malloc(t*sizeof(int)); //reserva de espaços de inteiros

 if(!p){
   printf("Erro\n");
   exit(1);
 } else{
   printf("alocação feita\n");
 }
 
for(i=0;i<6;i++){
  scanf("%d",&p[i]);

} 

for(i=0;i<6;i++){
  printf("%d ",p[i]);
}
p = (int *) realloc(p,2*sizeof(int)); //aumentar a memória, no caso, duplicou


free(p); //liberou o espaço de para
printf("%d",*p); //sai nada, pois o espaço foi liberado
  return 0;
}