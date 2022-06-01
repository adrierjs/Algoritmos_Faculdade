#include <iostream>
/*3 – Faça um programa em que o usuário informe um número até que o resultado 
da subtração desse número por 3 seja um número par. O programa deverá ter 
as seguintes saídas:
• Se o resultado da subtração for ímpar o programa deverá informar ao 
usuário: "O cálculo retornou um número ímpar! Tente novamente”. E 
solicitar outro número.
• Se o resultado da subtração for par o programa deverá informa ao usuário:
“O cálculo retornou um número par! Programa encerrado! ”.*/

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
