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
    return count > N / 2 ? index : -1;
}

int main(void)
{
    int A[] = {3, 4, 3, 2, 3, -1, 3, 3};
    printf("%d\n", solution(A, 8));
    return 0;
}
