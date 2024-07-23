#include <stdio.h>
#include <math.h>


int main() {

    float a, b, c, d, r1, r2, rp, ip;

    printf("Enter EQU ");
    scanf("%f %f %f", &a, &b, &c);

    d = pow(b, 2) - 4*a*c;
    if(d >= 0)
    {
        r1 = (-b + sqrt(d)) / 2*a;
        r2 = (-b - sqrt(d)) / 2*a;
        printf("r1 = %f , r2 = %f ", r1, r2);
    }
    else
    {
        rp = -b / 2*a;
        ip = sqrt(-d) / 2*a;
        printf("rp = %f , ip = %f ", rp, ip);
    }

    return 0;
}