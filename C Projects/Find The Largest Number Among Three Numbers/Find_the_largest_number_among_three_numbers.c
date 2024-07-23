#include <stdio.h>

int main () {

    int a, b, c;
    
    printf("Enter three numbers ");

    scanf("%d %d %d", &a, &b, &c);

    int largest = a;

    if (largest < b)
    {
        largest = b;
    }
    if(largest < c)
    {
        largest = c;
    }

    printf("Largest number is %d", largest);

    



    
    return 0;
}