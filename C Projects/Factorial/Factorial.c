#include <stdio.h>

int main () {

    int n;
    int factorial = 1;
    

    printf("Enter value of n ");
    scanf("%d", &n);


    int i = 1;
    while (i < n + 1)
    {
        factorial *= i;
        i++;
    }
    
    printf("%d", factorial);
    
    return 0;
}