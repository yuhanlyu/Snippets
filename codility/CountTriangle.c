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
    int answer = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1, k = i + 2; j < N - 1; ++j) {
            for (; k < N && A[i] + A[j] > A[k]; ++k) ;
            answer += k - j - 1;
        }
    }
    return answer;
}

int main(void)
{
    int A[] = {10, 2, 5, 1, 8, 12};
    printf("%d\n", solution(A, 6));
    return 0;
}
