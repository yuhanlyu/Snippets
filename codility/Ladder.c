#include <stdio.h>
#include <stdlib.h>

struct Results {
    int *C;
    int L;
};

struct Results solution(int A[], int B[], int L);
struct Results solution(int A[], int B[], int L)
{
    int fib[L + 1];
    fib[0] = 0;
    fib[1] = 1;
    fib[2] = 2;
    for (int i = 3; i <= L; ++i)
        fib[i] = (fib[i - 1] + fib[i - 2]) & 0x3FFFFFFF;
    struct Results result = {calloc(L, sizeof(int)), L};
    for (int i = 0; i < L; ++i)
        result.C[i] = fib[A[i]] & ((1 << B[i]) - 1);
    return result;
}

int main(void)
{
    int A[] = {4, 4, 5, 5, 1}, B[] = {3, 2, 4, 3, 1};
    struct Results result = solution(A, B, 5);
    for (int i = 0; i < 5; ++i)
        printf("%d ", result.C[i]);
    puts("");
    return 0;
}
