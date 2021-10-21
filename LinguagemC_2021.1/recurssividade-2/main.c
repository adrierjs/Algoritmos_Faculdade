#include <stdio.h>

int fat(int n){
  if (n==1 || n==0){
    return 1;
  }
return n*fat(n-1);
}




int main(void) {
  printf("Fatorial\n");
  
  int n;
  scanf("%d",&n);
  printf("O valor de fatorial é: %d",fat(n));
  return 0;
}