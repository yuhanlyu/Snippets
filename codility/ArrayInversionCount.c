#include <stdio.h>
#include <string.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    if (N <= 1)
        return 0;
    int left = solution(A, N / 2), right = solution(A + N / 2, N - N / 2);
    if (left == -1 || right == -1)
        return -1;
    int inversion = left + right, temp[N];
    for (int i = 0, first = 0, last = N / 2; i < N; ) {
        if (A[first] <= A[last])
            temp[i++] = A[first++];
        else {
            inversion += N / 2 - first;
            if (inversion >= 1000000000)
                return -1;
            temp[i++] = A[last++];
        }
        if (first == N / 2) {
            while (i < N)
                temp[i++] = A[last++];
        } else if (last == N) {
            while (i < N)
                temp[i++] = A[first++];
        }
    }
    memcpy(A, temp, N * sizeof(int));
    return inversion;
}

int main(void)
{
    int A[] = {-1, 6, 3, 4, 7, 4};
    int B[] = {1, 2, 3};
    printf("%d\n", solution(A, 6));
    printf("%d\n", solution(B, 3));
}
