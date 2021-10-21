#include <stdio.h>
#include <string.h>
int main(void) {
	
char senha[] = "adrier";
char tentativa[10];
int retorno;

printf("Digite a entrada \n");
fgets(tentativa,sizeof(tentativa),stdin);

retorno = strcmp(senha,tentativa);
printf("%d",retorno);

//insira o seu código

return(0);
}
