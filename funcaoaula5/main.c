#include <stdio.h>


int f_soma(int a, int b){
  return a+b;
}
void ler(){
  int a, b;
  printf("Digite um valor:");
  scanf("%d",&a);
  printf("Digite um valor:");
  scanf("%d",&b);
  printf("O valor é %d",f_soma(a,b));

  }

int main(void) {
  int a, b;
  ler();

  return 0;
}