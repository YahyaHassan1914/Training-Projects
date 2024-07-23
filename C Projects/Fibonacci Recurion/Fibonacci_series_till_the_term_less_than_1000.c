#include <stdio.h>

int main () {

    int first_term, second_term, temp;
    first_term = 0;
    second_term = 1;

    printf("%d %d\n", first_term, second_term);
    
    while (second_term <= 1000)
    {
        temp = second_term;
        second_term = second_term + first_term;
        first_term = temp;
        printf("%d\n", second_term);
    }
    
    return 0;
}