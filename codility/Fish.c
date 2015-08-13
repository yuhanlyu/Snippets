#include <stdio.h>

int solution(int A[], int B[], int N);
int solution(int A[], int B[], int N) 
{
    int stack[N], top = 0, result = 0;
    for (int i = N - 1; i >= 0; --i) {
        if (B[i] == 0) {
            stack[top++] = A[i];
        } else {
            for ( ; top > 0 && stack[top - 1] < A[i]; --top) ;
            if (top == 0)
                ++result;
        }
    }
    return result + top;
}

int main(void)
{
    int A[] = {4, 3, 2, 1, 5};
    int B[] = {0, 1, 0, 0, 0};

    printf("%d\n", solution(A, B, 5));
}
