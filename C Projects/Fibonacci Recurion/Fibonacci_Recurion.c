// #include <stdio.h>

// int f;

// int fibonacci(int n) {
//    if(n == 0){
//       return 0;
//    } else if(n == 1) {
//       return 1;
//    } else {
//       return (fibonacci(n-1) + fibonacci(n-2));
//    }
// }

// int main () {
//     int n;

//     printf("Enter Number ");
//     scanf("%d \n", &n);

//     for(int i = 0; i<n; i++)
//     {
//       printf("%d ",fibonacci(i));            
//     }
//     return 0;
// }



// C code to implement Fibonacci series
#include <stdio.h>
 
// Function for fibonacci
int fib(int n)
{
    // Stop condition
    if (n == 0)
        return 0;
 
    // Stop condition
    if (n == 1 || n == 2)
        return 1;
 
    // Recursion function
    else
        return (fib(n - 1) + fib(n - 2));
}
 
// Driver Code
int main()
{
    // Initialize variable n.
    int n;

    printf("Enter Number ");
    scanf("%d", &n);
    // scanf("\n");

    printf("Fibonacci series "
           "of %d numbers is: ",
           n);
 
    // for loop to print the fibonacci series.
    for (int i = 0; i < n; i++) {
        printf("%d ", fib(i));
    }
    return 0;
}