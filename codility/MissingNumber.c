#include <stdio.h>

int solution(int A[], int N)
{
    int flag = 0;
    for (int i = 0; i < N; ++i) {
        int index = A[i] > 0 ? A[i] - 1 : -(A[i]) - 1;
        if (index < N)
            A[index] = -A[index];
        else
            flag = 1;
    }
    if (flag == 0)
        return N + 1;
    for (int i = 0; i < N; ++i)
        if (A[i] > 0)
            return i + 1;
}

int main(void)
{
    int A[] = {2, 3, 1, 5};
    int B[] = {1};
    printf("%d\n", solution(A, 4));
    printf("%d\n", solution(B, 1));
}
