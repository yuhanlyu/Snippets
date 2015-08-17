#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Results {
    int *A;
    int M;
};

struct Results solution(int N, int P[], int Q[], int M);
struct Results solution(int N, int P[], int Q[], int M)
{
    int primeFactor[N + 1], count[N + 1];
    memset(primeFactor, 0, (N + 1) * sizeof(int));
    memset(count, 0, (N + 1) * sizeof(int));
    for (int i = 2; i * i <= N; ++i)
        if (primeFactor[i] == 0)
            for (int j = i * i; j <= N; j += i)
                if (primeFactor[j] == 0)
                    primeFactor[j] = i;
    for (int i = 4; i <= N; ++i) {
        count[i] = count[i - 1];
        if (primeFactor[i] != 0 && primeFactor[i / primeFactor[i]] == 0)
            ++count[i];
    }
    struct Results result = {calloc(M, sizeof(int)), M};
    for (int i = 0; i < M; ++i)
        result.A[i] = count[Q[i]] - count[P[i] - 1];
    return result;
}

int main(void)
{
    int P[] = {1, 4, 16}, Q[] = {26, 10, 20};
    struct Results result = solution(26, P, Q, 3);
    for (int i = 0; i < 3; ++i)
        printf("%d ", result.A[i]);
    puts("");
    return 0;
}
