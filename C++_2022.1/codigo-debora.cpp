#include <iostream>
/*3 � Fa�a um programa em que o usu�rio informe um n�mero at� que o resultado 
da subtra��o desse n�mero por 3 seja um n�mero par. O programa dever� ter 
as seguintes sa�das:
� Se o resultado da subtra��o for �mpar o programa dever� informar ao 
usu�rio: "O c�lculo retornou um n�mero �mpar! Tente novamente�. E 
solicitar outro n�mero.
� Se o resultado da subtra��o for par o programa dever� informa ao usu�rio:
�O c�lculo retornou um n�mero par! Programa encerrado! �.*/

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int main(int argc, char** argv) {
	int entrada;
	int parar = 0;
	while(parar != -1){
		cout<<"Insira um dado: "<<"\n";
		cin>> entrada;
		entrada -= 3;
		if(entrada % 2 ==0){
			cout<<"O calculo retornou um numero par! Programa encerrado!\n";
			parar = -1;
		} else{
			cout<<"O calculo retornou um numero impar! Tente novamente!\n";
		}
		
	};
	
	return 0;
}
