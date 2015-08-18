#include <stdio.h>

int solution(int N, int M);
int solution(int N, int M)
{
    int a = N, b = M;
    while ((a %= b) && (b %= a))
        ;
    return N / (a + b);
}

int main(void)
{
    printf("%d\n", solution(10, 4));
    return 0;
}
