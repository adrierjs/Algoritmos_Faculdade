#include <stdio.h>

int main(void) {
  int x = 2;
  int y = 8;
  int *p;//ponteiros
  int *q;//ponteiros

  p = &x; //p recebe o endereço de x
  q = &y;//q recebe o endereço de y

//a)
printf("O endereço de x é: %p \n",&x);
printf("E o valor de x é: %d\n", x);
//b)
printf("O valor de p: %p \n", p);
printf("E valor de *p: %d \n", *p);

//c)
printf("O endereço de y: %p \n", &y);
printf("E o valor de y: %d \n", y);

//d)
printf("O valor de q: %p\n", q);
printf("E o valor de *q: %d\n", *q);

//e)
printf("O endereço de p: %p\n", &p);
printf("E o endereço de q: %p", &q);

}