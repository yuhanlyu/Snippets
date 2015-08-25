#include <stdio.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    int sol = 0;
    for (int i = 0; i < N; ++i)
        sol ^= A[i];
    return sol;
}

int main(void)
{
    int A[] = {9, 3, 9, 3, 9, 7, 9};
    printf("%d\n", solution(A, 7));
}
