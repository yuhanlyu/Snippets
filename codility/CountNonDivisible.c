#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Results {
    int *C;
    int L;
};

struct Results solution(int A[], int N);
struct Results solution(int A[], int N)
{
    int count[2 * N + 1], factors[2 * N + 1];
    memset(count, 0, (2 * N + 1) * sizeof(int));
    memset(factors, 0, (2 * N + 1) * sizeof(int));
    for (int i = 0; i < N; ++i)
        ++count[A[i]];
    for (int i = 1; i <= 2 * N; ++i)
        factors[i] = N;
    for (int i = 1; i <= 2 * N; ++i) {
        if (count[i])
            for (int j = i; j <= 2 * N; j += i)
                factors[j] -= count[i];
    }
    struct Results result = {calloc(N, sizeof(int)), N};
    for (int i = 0; i < N; ++i)
        result.C[i] = factors[A[i]];
    return result;
}

int main(void)
{
    int A[] = {3, 1, 2, 3, 6};
    struct Results result = solution(A, 5);
    for (int i = 0; i < 5; ++i)
        printf("%d ", result.C[i]);
    puts("");
    return 0;
}
