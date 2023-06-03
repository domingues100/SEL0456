#include <stdio.h>

int main(){
int a = 0;  //fn-2
int b = 1;  //fn-1
int aux;    //aux
int i;      //aux
int n;      //count number

printf("Digite a quantidade de termos desejada: ");     
scanf("%d", &n);                                        //gets the amount desired

for (i = 0; i < n; i++)
{
    aux = a;
    a = a + b;
    b = aux;
    printf("%d ", a);
}

return 0;
}
