#include <stdio.h>

int solution(int A[], int N)
{
    int result = 0;
    double min = (A[0] + A[1]) / 2.0;

    for (int i = 0; i < N - 1; ++i) {
        if (A[i] + A[i + 1] < min * 2.0) {
            min = (A[i] + A[i + 1]) / 2.0;
            result = i;
        }
        if (i < N - 2 && (A[i] + A[i + 1] + A[i + 2]) < min * 3.0) {
            min = (A[i] + A[i + 1] + A[i + 2]) / 3.0;
            result = i;
        }
    }
    return result;
}

int main(void)
{
    int A[] = {4, 2, 2, 5, 1, 5, 8};
    int B[] = {1, 2};
    int C[] = {1, 2, 1, 1};
    printf("%d\n", solution(A, 7));
    printf("%d\n", solution(B, 2));
    printf("%d\n", solution(C, 4));
    return 0;
}
