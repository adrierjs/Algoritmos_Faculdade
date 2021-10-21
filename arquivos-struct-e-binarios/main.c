#include <stdio.h>

typedef struct{
  char nome[10];
  int idade;
} Pessoa;



int main(void) {

  FILE *a;
  Pessoa p;

//ESCRITA
 //a = fopen("novo.txt","ab");

  //printf("Digite o nome e idade:");
  //scanf("%s",p.nome);
  //scanf("%d",&p.idade);

  //fwrite(&p, sizeof(Pessoa),1,a); //pega o nome e bota na lista
  
  a = fopen("novo.txt","rb");

fseek(a, 2*sizeof(Pessoa), SEEK_SET); //PARA MOSTRAR NA POSIÇÃO
  fread(&p, sizeof(Pessoa), 1, a);//mostra o que ta no arquivo

  printf("Nome %s e idade %d",p.nome,p.idade);





  return 0;
}