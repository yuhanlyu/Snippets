#include <stdio.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    int result = 0, curmin = A[0];
    for (int i = 1; i < N; ++i) {
        if (A[i] < curmin)
            curmin = A[i];
        else if (A[i] - curmin > result)
            result = A[i] - curmin;
    }
    return result;
}

int main(void)
{
    int A[] = {23171, 21011, 21123, 21366, 21013, 21367};
    printf("%d\n", solution(A, 6));
    return 0;
}
