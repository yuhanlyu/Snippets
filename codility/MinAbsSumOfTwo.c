#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

inline int abs(int x);
inline int abs(int x)
{
    return x >= 0 ? x : -x;
}

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
    if (A[0] >= 0)
        return A[0] + A[0];
    if (A[N - 1] <= 0)
        return -A[N - 1] - A[N - 1];
    int answer = INT_MAX;
    for (int l = 0, r = N - 1; l <= r; abs(A[l]) > abs(A[r]) ? ++l : --r) {
        int temp = abs(A[l] + A[r]);
        answer = temp < answer ? temp : answer;
    }
    return answer;
}

int main(void)
{
    int A[] = {1, 4, -3};
    int B[] = {-8, 4, 5, -10, 3};
    printf("%d\n", solution(A, 3));
    printf("%d\n", solution(B, 5));
    return 0;
}
