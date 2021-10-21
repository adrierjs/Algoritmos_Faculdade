#include <stdio.h>

int main(void) {
  float n1, n2, n3, n4;
  float media;
  printf("Digite a 1° nota\n");
  scanf("%f",&n1);
  printf("Digite a 2° nota\n");
  scanf("%f",&n2);
  printf("Digite a 3° nota\n");
  scanf("%f",&n3);
  printf("Digite a 4° nota\n");
  scanf("%f",&n4);
  media = (n1+n2+n3+n4)/4;
  if (media>=7.0){
    printf("Aprovado %f",media);
  }
  else if(media<7.0 && media >5.0){
    printf("Prova final %f.2",media);
  }
  else{
    printf("Reprovado %f.2",media);
  }
  
  




  return 0;
}