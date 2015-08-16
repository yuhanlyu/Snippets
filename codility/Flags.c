#include <stdio.h>
#include <math.h>

// This is a sqrt(n) lg n solution, which is faster than official solution
int solution(int A[], int N);
int solution(int A[], int N)
{
    int last = A[N - 1], peak = N, low = 0;
    if (N < 3)
        return 0;
    for (int i = N - 1; i >= 1; --i) {
        if (A[i] > last && A[i] > A[i - 1])
            peak = i;
        last = A[i];
        A[i] = peak;
    }
    A[0] = peak;
    for (int high = sqrt(N) + 1; low <= high;) {
        int mid = (low + high) / 2, j = 1 - mid, found = 1;
        for (int i = 0; i < mid; ++i) {
            if (j + mid >= N) {
                found = 0;
                break;
            }
            j = A[j + mid];
        }
        if (!found || j >= N)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return low - 1;
}

int main(void)
{
    int A[] = {1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2};
    int B[] = {1, 2, 1};
    int C[] = {1, 2, 3};
    int D[] = {1};
    printf("%d\n", solution(A, 12));
    printf("%d\n", solution(B, 3));
    printf("%d\n", solution(C, 3));
    printf("%d\n", solution(D, 1));
    return 0;
}
