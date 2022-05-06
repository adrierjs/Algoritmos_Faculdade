#include <iostream>
#include <string>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	struct pessoa{
		string nome;
		int idade;
		string endereco;
	};
	
	
	pessoa p1;
	p1.nome = "Adrier";
	
	
//	cout<<p1.nome;
	cout<<"Digite a sua idade: ";
	cin>>p1.idade;
	cout<<"Digite o seu endereco";
	cin>>p1.endereco;
	
	cout<<"\n**Informacoes do usuario**\n";
	cout<< "Nome: "<<p1.nome;
	cout<< "\nIdade: "<< p1.idade;
	cout<<"\nEndereco: "<<p1.endereco;
	return 0;
}
