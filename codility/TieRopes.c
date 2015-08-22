#include <stdio.h>

int solution(int K, int A[], int N);
int solution(int K, int A[], int N)
{
    int answer = 0;
    for (int i = 0, current = 0; i < N; ++i) {
        current += A[i];
        if (current >= K) {
            ++answer;
            current = 0;
        }
    }
    return answer;
}

int main(void)
{
    int A[] = {1, 2, 3, 4, 1, 1, 3};
    printf("%d\n", solution(4, A, 7));
}
