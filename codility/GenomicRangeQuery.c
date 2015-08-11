#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Results {
    int *A;
    int M;
};

struct Results solution(char *S, int P[], int Q[], int M)
{
    unsigned length = strlen(S);
    int A[length], C[length], G[length], T[length];

    for (int i = 0; i < length; ++i) {
        if (i == 0)
            A[i] = C[i] = G[i] = T[i] = 0;
        else {
            A[i] = A[i - 1];
            C[i] = C[i - 1];
            G[i] = G[i - 1];
            T[i] = T[i - 1];
        }
        switch (S[i]) {
            case 'A':
                ++A[i];
                break;
            case 'C':
                ++C[i];
                break;
            case 'G':
                ++G[i];
                break;
            case 'T':
                ++T[i];
                break;
        }
    }

    struct Results result = {calloc(M, sizeof(int)), M};
    for (int i = 0; i < M; ++i) {
        if (A[Q[i]] - (P[i] > 0 ? A[P[i] - 1] : 0) > 0)
            result.A[i] = 1;
        else if (C[Q[i]] - (P[i] > 0 ? C[P[i] - 1] : 0) > 0)
            result.A[i] = 2;
        else if (G[Q[i]] - (P[i] > 0 ? G[P[i] - 1] : 0) > 0)
            result.A[i] = 3;
        else
            result.A[i] = 4;
    }
    return result;
}

int main(void)
{
    char S[] = "CAGCCTA";
    int P[] = {2, 5, 0}, Q[] = {4, 5, 6};
    struct Results result = solution(S, P, Q, 3);
    for (int i = 0; i < 3; ++i)
        printf("%d ", result.A[i]);
    puts("");
    return 0;
}
