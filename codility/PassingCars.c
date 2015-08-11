#include <stdio.h>

int solution(int A[], int N) 
{
    int result = 0, zeros = 0;
    for (int i = 0; i < N; ++i)
        if (A[i] == 1) {
            if (1000000000 - zeros >= result)
                result += zeros;
            else
                return -1;
        } else
            ++zeros;
    return result;
}

int main(void)
{
    int A[] = {0, 1, 0, 1, 1};
    printf("%d\n", solution(A, 5));
    return 0;
}
