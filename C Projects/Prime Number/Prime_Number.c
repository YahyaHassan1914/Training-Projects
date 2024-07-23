#include <stdio.h>

int main () {

    int n, i, flag;
    
    flag = 1;
    i = 2;

    printf("Input Number : ");
    scanf("%d", &n);
    
    for (int i = 2; i < n/2; i++)
    {
        if (n % i == 0)
        {
            flag = 0;
        }
        
    }
    
    if (flag == 0)
    {
        printf("Number is not prime");
    }
    else
    {
        printf("Number is prime");
    }

    
    return 0;
}