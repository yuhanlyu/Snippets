#include <stdio.h>
#include <string.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    int fib[26] = {0, 1}, F[N + 1];
    for (int i = 2; i <= 25; ++i)
        fib[i] = fib[i - 1] + fib[i - 2];
    memset(F, 255, (N + 1) * sizeof(int)); 
    for (int i = 2; i <= 25 && fib[i] <= N + 1; ++i)
        if (A[fib[i] - 1] == 1 || fib[i] == N + 1)
            F[fib[i] - 1] = 1;
    for (int i = 0; i <= N; ++i) {
        if ((i == N || A[i] == 1) && F[i] < 0) {
            int min = N + 1;
            for (int j = 2; j <= 25 && i - fib[j] >= 0; ++j) {
                if (F[i - fib[j]] > 0 && F[i - fib[j]] < min)
                    min = F[i - fib[j]];
            }
            if (min != N + 1)
                F[i] = min + 1;
        }
    }
    return F[N];
}

int main(void)
{
    int A[] = {0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0};
    int B[] = {0};
    int C[] = {0, 0, 0};
    printf("%d\n", solution(A, 11));
    printf("%d\n", solution(B, 1));
    printf("%d\n", solution(C, 3));
    return 0;
}
