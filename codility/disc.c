#include <stdio.h>

/* Codility Beta 2010 */
int solution ( int A[], int N );
int solution ( int A[], int N ) 
{
    unsigned int start[1000000], end[1000000], active, sol, i;

    /* Store the start and end point in the array */
    for ( i = 0; i < N; ++i ) {
        ++start[ i >= A[i] ? i - A[i] : 0 ];
        ++end[ A[i] + i >= N ? N - 1 : A[i] + i ];
    }
    /* Plane sweep */
    for ( active = sol = i = 0; i < N; ++i ) {
        sol += active * start[ i ] + (start[ i ] * (start[ i ] - 1)) / 2;
        if (sol > 10000000)
            return -1;
        active += start[ i ] - end[ i ];
    }
    return sol;
}

int main(void)
{
    int A[] = {1, 5, 2, 1, 4, 0};
    printf( "%d\n", solution(A, 6) );
    return 0;
}
