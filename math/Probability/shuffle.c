#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Remove modulo bias */
int rand_int( int n );
int rand_int( int n )
{
    int     r;

    while ( ( r = rand() ) >= RAND_MAX - ( RAND_MAX % n ) ) ;
    return r % n;
}

/* Fisher–Yates shuffle */
void shuffle( int array[], int n );
void shuffle( int array[], int n )
{
    for ( int i = n - 1; i >= 1; --i ) {
        int r = rand_int( i + 1 );
        int temp = array[ r ];
        array[ r ] = array[ i ];
        array[ i ] = temp;
    }
}

int main( void )
{
    int     array[ 10 ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    srand( time( NULL ) );
    shuffle( array, 10 );
    for ( int i = 0; i < 10; ++i )
        printf( "%d ", array[ i ] );
    puts( "" );
    return 0;
}
