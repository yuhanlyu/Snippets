#include <stdio.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    int result = A[0], curSum = A[0];
    for (int i = 1; i < N; ++i) {
        if (curSum < 0)
            curSum = 0;
        curSum += A[i];
        if (curSum > result)
            result = curSum;
    }
    return result;
}

int main(void)
{
    int A[] = {3, 2, -6, 4, 0};
    int B[] = {-3, -2};
    printf("%d\n", solution(A, 5));
    printf("%d\n", solution(B, 2));
    return 0;
}
