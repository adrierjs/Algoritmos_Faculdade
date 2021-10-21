#include <stdio.h>

void valores(int *a, int *b);//lembrar de declarar no escopo para nao dar erro.
// O VALOR COM REFERENCIA CONSERVA O VALOR ANTERIOR DO CÓDIGO, OU SEJA O VALOR DE A E B FORAM CONSERVADOS NA MEMÓRIA.
int main(void) {
  int n1 = 4;
  int n2 = 5;
  printf("Valores antes da função: %d, %d\n",n1,n2);

  valores(&n1,&n2);
  printf("Valores depois da função: %d, %d\n",n1,n2);
  return 0;
}
void valores (int *a, int *b){
  *a=*a+1;
  *b=*b+1;
  printf("Valores dentro da função: %d, %d\n",*a,*b);
}