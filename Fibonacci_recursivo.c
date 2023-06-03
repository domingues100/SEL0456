#include <stdio.h>

int fibonacci (int n){
    int fibo;
    
    if (n == 1 || n == 2) {                                 //númbers that function can't use
        return(1);
    }
    
    fibo = (fibonacci(n-1) + fibonacci (n-2));
    
    return (fibo);                                            //function
}

int main() {
    int n;
    int i;

    printf("Digite a quantidade de termos desejada: ");     
    scanf("%d", &n);                                        //gets the amount desired

    for(i=1; i <= n; i++) {                                 //loop that gets the values calling the function i times
        printf("%d ", fibonacci(i));
    }

    return(0);
}
