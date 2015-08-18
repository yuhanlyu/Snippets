#include <stdio.h>

int gcd(int a, int b);
int gcd(int a, int b)
{
    while ((a %= b) && (b %= a)) ;
    return a + b;
}

int check(int a, int d);
int check(int a, int d)
{
    a /= d;
    for (int temp; d % a != 0; a /= temp) {
        temp = gcd(a, d);
        if(temp == 1)
            return 0;
    }
    return 1;
}

int solution(int A[], int B[], int Z);
int solution(int A[], int B[], int Z)
{
    int result = 0;
    for (int i = 0; i < Z; ++i) {
        int d = gcd(A[i], B[i]);
        if (check(A[i], d) && check(B[i], d))
            ++result;
    }
    return result;
}

int main(void)
{
    int A[] = {15, 10, 3}, B[] = {75, 30, 5};
    printf("%d\n", solution(A, B, 3));
    return 0;
}
