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
    int result = 0;
    for (int i = 0; i < N; ++i)
        if (i == 0 || A[i] != A[i - 1])
            ++result;
    return result;
}

int main(void)
{
    int A[] = {2, 1, 1, 2, 3, 1};

    printf("%d\n", solution(A, 6));
}
