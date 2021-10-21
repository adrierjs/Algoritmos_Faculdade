#include <stdio.h>
int main(void) {
  char nomes[2][10][10];/** linha; coluna; tamanho do vetor**/
  float notas[2][10][2]; 
  int i, j, k;
  int t=2;//turma
  int al=2;//alunos
  int nt=2;//notas por aluno
for (i=0;i<t;i++){
    for (j=0;j<al;j++){
      printf("Turma %d\nAluno %d:",i+1,j+1);
      scanf("%s",nomes[i][j]);
    }
}
for (i=0;i<t;i++){//turma
  for(j=0;j<al;j++){//alunos
    for(k=0;k<nt;k++){//notas por alunos
    printf("Turma %d\nAluno %s\nDigite a nota: ",i+1,nomes[i][j]);
        scanf("%f",&notas[i][j][k]); 
    }
  }
}
for(i=0;i<t;i++){
  printf("Turma %d\n",i+1);
  for(j=0;j<al;j++){
     printf("%s:\n",nomes[i][j]);//alunos
    for(k=0;k<nt;k++){
      printf("%.2f\n",notas[i][j][k]);
    }
  }
}
return 0;
}