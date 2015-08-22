#include <stdio.h>

int solution(int A[], int B[], int N);
int solution(int A[], int B[], int N)
{
    int answer = 0;
    for (int i = 0, end = -1; i < N; ++i) {
        if (A[i] > end) {
            ++answer;
            end = B[i];
        }
    }
    return answer;
}

int main(void)
{
    int A[] = {1, 3, 7, 9, 9}, B[] = {5, 6, 8, 9, 10};
    printf("%d\n", solution(A, B, 5));
}
