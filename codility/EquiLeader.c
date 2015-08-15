#include <stdio.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    int count = 1, index = 0;
    for (int i = 1; i < N; ++i) {
        if (count == 0) {
            index = i;
            count = 1;
        } else {
            count += (A[index] == A[i] ? 1 : -1);
        }
    }
    for (int i = count = 0; i < N; ++i) {
        if (A[index] == A[i])
            ++count;
    }
    if (count <= N / 2) 
        return 0;
    int c = 0, result = 0;
    for (int i = 0; i < N; ++i) {
        if (A[index] == A[i])
            ++c;
        if (c > (i + 1) / 2 && (count - c) > (N - i - 1) / 2)
            ++result;
    }
    return result;
}

int main(void)
{
    int A[] = {4, 3, 4, 4, 4, 2};
    printf("%d\n", solution(A, 6));
    return 0;
}
