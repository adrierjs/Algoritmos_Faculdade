#include<stdio.h>
#include<stdlib.h>

//Usando typedef na struct para encurtar o comando na declaração
typedef struct
{
  int matricula ;
  float nota;
}tAluno;

int main (void)
{
  //a1 é uma struct do tipo tAluno
  tAluno a1 ; 
  
  //*ptrAluno é um ponteiro do tipo tAluno que
  //recebe o endereço de a1;
  tAluno *ptrAluno = &a1;   
  
  //Atribuindo valores para os membros da struct a1
  a1.matricula =555;
  a1.nota = 8.0;
  
  //exibindo dados usando a struct diretamente usando .
  printf ("matricula: %d nota: %.2f \n",a1.matricula,a1.nota);
  
  //Podemos atribuir ou acessar um valor usando o ponteiro (*ptrAluno)
  (*ptrAluno).nota = 8.5;
  
  //exibindo dados usando um ponteiro para struct
  printf ("\nmatricula: %d nota: %.2f \n",(*ptrAluno).matricula,(*ptrAluno).nota);
  
  //ptrAluno-> substitui a notação (*ptrAluno). de forma mais intuitiva  
  
  //atribuindo um novo valor para a nota usando ptrAluno->
  ptrAluno->nota = 9.0;
  
  //portanto (*ptrAluno).nota é o mesmo que usar ptrAluno->nota
  
  printf ("\nmatricula: %d nota: %.2f \n",ptrAluno->matricula,ptrAluno->nota);
  
  return 0;
}