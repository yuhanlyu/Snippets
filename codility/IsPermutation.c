#include <stdio.h>

int solution(int A[], int N)
{
    int visited[N];

    for (int i = 0; i < N; ++i) {
        visited[i] = 0;
        if (A[i] <= 0 || A[i] > N)
            return 0;
    }
    for (int i = 0; i < N; ++i) {
        if (visited[A[i] - 1] == 0)
            visited[A[i] - 1] = 1;
        else
            return 0;
    }
    return 1;
}

int main(void)
{
    int A[] = {4, 1, 3, 2};
    int B[] = {4, 1, 3};

    printf("%d\n", solution(A, 4));
    printf("%d\n", solution(B, 3));
}
