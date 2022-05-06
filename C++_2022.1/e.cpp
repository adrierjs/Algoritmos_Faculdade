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
	
	struct moto{
		string nome[10];
		string endereco[50];
		string telefone[15];
		int idade[3];
	};
	
	
	moto m1;
	int tam = 2;

	for(int i = 0; i<tam; i++){
	
		cout<<"Digite o nome: ";
		cin>>m1.nome[i];
		cout<<"Digite a sua idade: ";
		cin>>m1.idade[i];
		cout<<"Digite o seu endereco: ";
		cin>>m1.endereco[i];
		cout<<"Digite o telefone: ";
		cin>>m1.telefone[i];
		
		cout<<"\n************\n";
		
	}
	
	for(int i=0; i<tam;i++){
		cout<<"Nome: "<<m1.nome[i]<<"\n";
		cout<<"Idade: "<<m1.idade[i]<<"\n";
		cout<<"Endereco: "<<m1.endereco[i]<<"\n";
		cout<<"Telefone: "<<m1.telefone[i]<<"\n";
		cout<<"\n************\n";
		
		
		}
	
	return 0;
	
	
}
