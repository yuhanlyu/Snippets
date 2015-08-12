#include <stdio.h>

void hailstones( int n );

int main( void )
{
    int     n;

    scanf( "%d", &n );
    hailstones( n );
    return 0;
}

// Test Collatz conjecture
void hailstones( int n )
{
    while ( n != 1 ) {
        n = n % 2 == 0 ? ( n / 2 ) : ( 3 * n + 1 );
        printf( "%d\n", n );
    }
}

