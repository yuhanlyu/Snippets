#include <stdio.h>

int solution(int A, int B, int K)
{
    if (A % K)
        A += K - A % K;
    return A <= B ? (B - A) / K + 1 : 0;
}

int main(void)
{
    printf("%d\n", solution(6, 11, 2));
    printf("%d\n", solution(6, 12, 2));
    printf("%d\n", solution(6, 6, 2));
    printf("%d\n", solution(7, 7, 2));
    return 0;
}
