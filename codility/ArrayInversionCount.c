#include <stdio.h>
#include <string.h>

int solution(int A[], int N);
int solution(int A[], int N)
{
    int inversion = 0;
    for (int size = 1; size < N; size *= 2) {
        for (int start = 0; start < N - size; start += 2 * size) {
            int end = (start + 2*size - 1) >= N ? N - 1 : start + 2 * size - 1;
            int mid = start + size - 1, temp[end - start + 1];
            for (int i = 0, first = start, last = mid + 1; i <= end - start;) {
                if (A[first] <= A[last])
                    temp[i++] = A[first++];
                else {
                    inversion += mid - first + 1;
                    if (inversion >= 1000000000)
                        return -1;
                    temp[i++] = A[last++];
                }
                if (first == mid + 1) {
                    while (i <= end - start)
                        temp[i++] = A[last++];
                } else if (last == end + 1) {
                    while (i <= end - start)
                        temp[i++] = A[first++];
                }
            }
            memcpy(A + start, temp, (end - start + 1) * sizeof(int));
        }
    }
    return inversion;
}

int main(void)
{
    int A[] = {-1, 6, 3, 4, 7, 4};
    int B[] = {1, 2, 3};
    printf("%d\n", solution(A, 6));
    printf("%d\n", solution(B, 3));
}
