#include <stdio.h>
#include <string.h>

int solution(int M, int A[], int N);
int solution(int M, int A[], int N)
{
    int result = 0, used[M + 1], begin = -1;
    memset(used, 255, (M + 1) * sizeof(int));
    for (int i = 0; i < N; ++i) {
        if (used[A[i]] > begin)
            begin = used[A[i]];
        result += i - begin;
        used[A[i]] = i;
        if (result >= 1000000000)
            return 1000000000;
    }
    return result;
}

int main(void)
{
    int A[] = {3, 4, 5, 5, 2};
    printf("%d\n", solution(6, A, 5));
    return 0;
}
