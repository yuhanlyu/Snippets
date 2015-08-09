#include <stdio.h>

int solution(int A[], int N)
{
    int xor = 0;
    for (int i = 1; i <= N + 1; ++i)
        xor ^= i;
    for (int i = 0; i < N; ++i)
        xor ^= A[i];
    return xor;
}

int main(void)
{
    int A[] = {2, 3, 1, 5};
    int B[] = {1};
    printf("%d\n", solution(A, 4));
    printf("%d\n", solution(B, 1));
}
