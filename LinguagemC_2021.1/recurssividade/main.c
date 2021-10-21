#include <stdio.h>


int fat(int n){


/*
n=5 -> n*fat(n-1) = 5*24 = 120 
n=4 -> n*fat(n-1) = 4*6 = 24
n=3 -> n*fat(n-1) = 3*2 = 6
n=2 -> n*fat(n-1) = 2*1 = 2
n=1 -> 1

*/
if (n==1) {
	return 1;
}
else if(n==0){
  return 1;
}


return n*fat(n-1);
	
}


int main(void)
{
printf("Fatorial\n");

int n;

scanf("%d", &n);

// n=5; 5! -> 5x4x3x2x1 = 120

printf("O valor da soma total eh %d", fat(n));

return(0);
}