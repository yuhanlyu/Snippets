#include <stdio.h>

int solution(int A[], int N);
int solution(int H[], int N)
{
    int stack[N], top = -1, result = 0;
    for (int i = 0; i < N; ++i) {
        for (; top >= 0 && stack[top] > H[i]; --top) ;
        if (top == -1 || stack[top] < H[i]) {
            stack[++top] = H[i];
            ++result;
        }
    }
    return result;
}

int main(void)
{
    int H[] = {8, 8, 5, 7, 9, 8, 7, 4, 8};
    printf("%d\n", solution(H, 9));
}
