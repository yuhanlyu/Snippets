#include <stdio.h>

/* Codility Alpha 2010 */
int solution ( int A[], int N );
int solution ( int A[], int N ) {
    char set[ 1000000 ] = { 0 };
    int sol = 0, i;

    for (i = 0; i < N; ++i) {
        if (set[ A[i] ] == 0) {
            set[ A[i] ] = 1;
            sol = i;
        }
    }
    return sol;
}

int main(void)
{
    int A[] = { 2, 2, 1, 0, 1 };
    printf( "%d\n", solution(A, 5) );
}
