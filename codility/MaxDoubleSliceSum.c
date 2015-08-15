#include <stdio.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    int result = 0, curSum = A[1], curDS = 0;
    for (int i = 2; i < N - 1; ++i) {
        curDS = curSum > curDS + A[i] ? curSum : curDS + A[i];
        if (curDS > result)
            result = curDS;
        curSum += A[i];
        if (curSum < 0)
            curSum = 0;
    }
    return result;
}

int main(void)
{
    int A[] = {3, 2, 6, -1, 4, 5, -1, 2};
    printf("%d\n", solution(A, 8));
    return 0;
}
