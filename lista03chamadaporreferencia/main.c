#include <stdio.h>

void mudar_valor(int*x, int*y, int*temp){
  *temp =*x; // temp recebe valor a
  *x=*y; //x recebe valor b
  *y =*temp;// y recebe temp
  printf("Valores dentro da função: %d, %d, %d\n",*temp,*x,*y);
}

int main(void) {
  int a, b, temp;
  a = 5;
  b = 4;
  temp = 0; //temp = 0 só para ficar organizado
  printf("valores antes da função: %d, %d, %d\n",a,b,temp);
  mudar_valor(&a, &b, &temp);
  printf("Valores depois da função: %d, %d, %d",a,b,temp);
  return 0;

}


