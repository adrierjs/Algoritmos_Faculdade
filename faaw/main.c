#include <stdio.h>

int main(void) {
 


  float notas [2][3][2];

  int i,j,k;


  char nomes[2][3][5];/*{{"mar", "rio", "ceu"},{"mar", "rio", "ceu"}}; // 2x3*/


  /*

  mar rio ceu

  mar rio ceu

  */
 for (i=0;i<2;i++){

    for (j=0;j<3;j++){

    scanf(" %s",nomes[i][j]);

    }


  for (i=0;i<2;i++){

    for (j=0;j<3;j++){

    printf(" %s",nomes[i][j]);

    }

    printf("\n");

  }
 }
  
  return 0;

  }