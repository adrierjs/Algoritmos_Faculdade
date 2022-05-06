#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	struct moto{
		string nome;
		string placa;
		moto*prox; //Um ponteiro para apontar p outro ponteiro
	};
	
	
	
	moto*m1 = new moto;//criei o ponteiro para apontar para outro ponteiro
	
	m1->nome = "honda\n";
	m1-> placa = "MMM24";
	m1-> prox = NULL;
	
	cout<<m1->nome;
	cout<<m1->placa;
	cout<<m1->prox;
	
	
	moto*m2 = new moto;
	m2->nome = "Yamaha\n";
	m2-> placa = "0000";
	m1->prox = m2; //m1 aponta para m2
	
	cout<<m2->nome;
	cout<<m2->placa;
	cout<<m2;
	
	
	return 0;
	
	
}
