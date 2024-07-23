#include <stdio.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Function declarations
float add(float x, float y) {
    return x + y;
}

float subtract(float x, float y) {
    return x - y;
}

float multiply(float x, float y) {
    return x * y;
}

float divide(float x, float y) {
    if (y != 0) {
        return x / y;
    } else {
        printf("Error! Division by zero.\n");
        return 0;  // Return 0 on division by zero
    }
}

float power(float x, float y) {
    return pow(x, y);
}

float sqrt_func(float x) {
    if (x >= 0) {
        return sqrt(x);
    } else {
        printf("Error! Square root of a negative number.\n");
        return 0;  // Return 0 for square root of negative number
    }
}

float log_func(float x, float base) {
    if (x > 0) {
        return log10(x) / log10(base);
    } else {
        printf("Error! Logarithm of non-positive number.\n");
        return 0;  // Return 0 for logarithm of non-positive number
    }
}

float sin_func(float x) {
    return sin(x * M_PI / 180.0);
}

float cos_func(float x) {
    return cos(x * M_PI / 180.0);
}

float tan_func(float x) {
    return tan(x * M_PI / 180.0);
}

int factorial(int x) {
    if (x >= 0) {
        int result = 1;
        for (int i = 1; i <= x; ++i) {
            result *= i;
        }
        return result;
    } else {
        printf("Error! Factorial of a negative number.\n");
        return 0;  // Return 0 for factorial of negative number
    }
}

void menu() {
    printf("Advanced Calculator\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Power\n");
    printf("6. Square Root\n");
    printf("7. Logarithm\n");
    printf("8. Sine\n");
    printf("9. Cosine\n");
    printf("10. Tangent\n");
    printf("11. Factorial\n");
    printf("12. Exit\n");
}

int main() {
    while (1) {
        menu();
        printf("Select operation (1-12): ");
        int choice;
        scanf("%d", &choice);
        
        if (choice == 12) {
            printf("Exiting the calculator.\n");
            break;
        }
        
        float x, y;
        if (choice >= 1 && choice <= 5) {
            printf("Enter first number: ");
            scanf("%f", &x);
            printf("Enter second number: ");
            scanf("%f", &y);
        }
        
        switch (choice) {
            case 1:
                printf("Result: %.2f\n", add(x, y));
                break;
            case 2:
                printf("Result: %.2f\n", subtract(x, y));
                break;
            case 3:
                printf("Result: %.2f\n", multiply(x, y));
                break;
            case 4:
                printf("Result: %.2f\n", divide(x, y));
                break;
            case 5:
                printf("Result: %.2f\n", power(x, y));
                break;
            case 6:
                printf("Enter number: ");
                scanf("%f", &x);
                printf("Result: %.2f\n", sqrt_func(x));
                break;
            case 7:
                printf("Enter number: ");
                scanf("%f", &x);
                float base;
                printf("Enter base (default is 10): ");
                scanf("%f", &base);
                base = (base == 0) ? 10 : base;
                printf("Result: %.2f\n", log_func(x, base));
                break;
            case 8:
                printf("Enter angle in degrees: ");
                scanf("%f", &x);
                printf("Result: %.2f\n", sin_func(x));
                break;
            case 9:
                printf("Enter angle in degrees: ");
                scanf("%f", &x);
                printf("Result: %.2f\n", cos_func(x));
                break;
            case 10:
                printf("Enter angle in degrees: ");
                scanf("%f", &x);
                printf("Result: %.2f\n", tan_func(x));
                break;
            case 11:
                printf("Enter number: ");
                scanf("%d", &x);
                printf("Result: %d\n", factorial(x));
                break;
            default:
                printf("Invalid input. Please enter a number between 1 and 12.\n");
        }
        
        printf("Press Enter to continue...\n");
        while (getchar() != '\n');  // Clear input buffer
        getchar();  // Wait for Enter key
        printf("\n");
    }
    
    return 0;
}
