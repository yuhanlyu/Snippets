#include <stdio.h>

int solution(int K, int M, int A[], int N);
int solution(int K, int M, int A[], int N)
{
    int low = 0, high = 0;
    for (int i = 0; i < N; ++i) {
        high += A[i];
        low = (low < A[i]) ? A[i] : low;
    }
    while (low <= high) {
        int mid = low + (high - low) / 2, count = 0;
        for (int j = 0; j < N && count <= K; ++count) {
            for (int sum = 0; j < N && sum + A[j] <= mid; ++j)
                sum += A[j];
        }
        if (count <= K)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return low;
}

int main(void)
{
    int A[] = {2, 1, 5, 1, 2, 2, 2};
    printf("%d\n", solution(3, 5, A, 7));
    return 0;
}
