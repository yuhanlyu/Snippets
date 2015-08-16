#include <stdio.h>
#include <math.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    if (N < 3)
        return 0;
    int peaks[N];
    peaks[0] = peaks[1] = 0;
    for (int i = 2; i < N; ++i) {
        peaks[i] = peaks[i - 1];
        if (A[i - 1] > A[i - 2] && A[i - 1] > A[i])
            ++peaks[i];
    }
    for (int size = 3; size <= N; ++size) {
        if (N % size == 0) {
            int pos = size;
            for (; pos < N; pos += size) {
                if (peaks[pos] == peaks[pos - size])
                    break;
            }
            if (pos == N && peaks[N - 1] != peaks[N - size])
                return N / size;
        }
    }
    return 0;
}

int main(void)
{
    int A[] = {1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2};
    int B[] = {1, 2, 1};
    int C[] = {1, 2, 1, 2, 3, 1};
    int D[] = {1};
    printf("%d\n", solution(A, 12));
    printf("%d\n", solution(B, 3));
    printf("%d\n", solution(C, 6));
    printf("%d\n", solution(D, 1));
    return 0;
}
