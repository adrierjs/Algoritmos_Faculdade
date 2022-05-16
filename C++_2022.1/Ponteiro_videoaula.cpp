#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int main(int argc, char** argv) {
	int *p;
	int vetor[3];
	vetor[0] = 1;
	for(int i=0; i<3;i++){
	
	p=&vetor[i];
	cout<<"\n"<<p <<"\n";
}
	return 0;
}
