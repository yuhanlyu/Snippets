#include <stdio.h>

int solution(int A[], int N)
{
    int sumRight = 0, sumLeft = 0, minDiff = 1 << 30;

    for (int i = 0; i < N; ++i)
        sumRight += A[i];
    for (int i = 0; i < N - 1; ++i) {
        sumLeft += A[i];
        sumRight -= A[i];
        int diff = sumLeft - sumRight;
        diff = diff >= 0 ? diff : -diff;
        minDiff = minDiff < diff ? minDiff : diff;
    }
    return minDiff;
}

int main(void)
{
    int A[] = {3, 1, 2, 4, 3};
    printf("%d\n", solution(A, 5));
}
