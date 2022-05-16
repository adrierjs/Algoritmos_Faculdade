/*
	Laboratório de estrutura de dados
	Discente: Adrier José Silva dos Santos - 4° período - Diurno
	Docente: Allan Villar de Carvalho 

*/

#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
		struct Pessoa{
			string nome;
			int idade;
			Pessoa*prox; /*Um ponteiro que irá apontar para a próxima caixa*/
		
	};
	int tam = 3;
	Pessoa * p[tam];
	
	for(int i=0; i<tam;i++){
		p[i] = new Pessoa;//inicilizando o objeto na posicão i
		cout<<"Dados pessoa "<<i+1;
		cout<<"\nDigite o nome: ";
		cin>>p[i]->nome;
		cout<<"Digite a idade: ";
		cin>>p[i]->idade;
		
	}
	
	for(int i=0; i<tam; i++){
		cout<<"Dados da pessoa "<<i+1<<"\n";
		cout<<"Nome: "<<p[i]->nome<<"\n";
		cout<<"Idade: "<<p[i]->idade<<"\n";	}
	
	
		
	
	return 0; }
