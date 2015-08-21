#include <stdio.h>
#define ABS(X) ((X >= 0) ? (X) : (-X))

int solution(int A[], int N);
int solution(int A[], int N)
{
    int current = ABS(A[0]) > ABS(A[N - 1]) ? ABS(A[0]) : ABS(A[N - 1]), left;
    for (left = 0; left < N && A[left] == -2147483648; ++left) ;
    int result = left > 0 ? 1 : 0;
    for (int right = N - 1; left <= right; ++result) {
        for (; ABS(A[left]) == current; ++left) ;
        for (; ABS(A[right]) == current; --right) ;
        current = ABS(A[left]) > ABS(A[right]) ? ABS(A[left]) : ABS(A[right]);
    }
    return result;
}

int main(void)
{
    int A[] = {-5, -3, -1, 0, 3, 6};
    printf("%d\n", solution(A, 6));
    return 0;
}
