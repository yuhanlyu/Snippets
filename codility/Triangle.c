#include <stdio.h>
#include <stdlib.h>

int compare(const void *p, const void *q);
int compare(const void *p, const void *q)
{
    int x = *(const int *)p;
    int y = *(const int *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
}

int solution(int A[], int N);
int solution(int A[], int N)
{
    qsort(A, N, sizeof(int), compare);
    for (int i = 1; i < N - 1; ++i)
        if (A[i + 1] - A[i] < A[i - 1])
            return 1;
    return 0;
}

int main(void)
{
    int A[] = {10, 2, 5, 1, 8, 20};
    int B[] = {10, 50, 5, 1};

    printf("%d\n", solution(A, 6));
    printf("%d\n", solution(B, 4));
    return 0;
}
