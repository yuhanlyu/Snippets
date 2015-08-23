#include <stdio.h>
#include <limits.h>

// Space complexity is O(1)
int solution(int A[], int N);
int solution(int A[], int N)
{
    int D[6] = {A[0], INT_MIN, INT_MIN, INT_MIN, INT_MIN, INT_MIN};
    for (int i = 1; i < N; ++i) {
        int max = INT_MIN;
        for (int j = 0; j < 6; ++j)
            if (D[j] > max)
                max = D[j];
        D[i % 6] = max + A[i];
    }
    return D[(N - 1) % 6];
}

int main(void)
{
    int A[] = {1, -2, 0, 9, -1, -2};
    int B[] = {2, 3};
    int C[] = {-1, 3};
    printf("%d\n", solution(C, 2));
}
