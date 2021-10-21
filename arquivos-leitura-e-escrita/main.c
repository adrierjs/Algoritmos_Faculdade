#include <stdio.h>

int main(void) {
  FILE *a, *e; 
  float n1,n2,media;
  
  a = fopen("exemplo.txt","r");
// w = cria novo arquivo 
// r = abre arquivo
// a = vai adicionar no que ja existe
e = fopen("novo.txt", "a");

while (fscanf(a,"%f %f",&n1,&n2) ==2){
  media = (n1+n2)/2;

  fprintf(e,"%.2f",media);
  if(media >=7){
  fprintf(e,"= aprovado\n");
  } else{
    fprintf(e,"= reprovado\n");
  }
}
//fechar arquivos
fclose(a);
fclose(e);



  return 0;
}