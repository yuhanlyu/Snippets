#include <stdio.h>

/** Computes the solution of tower of Hanoi with n disks */
void hanoi( unsigned int n );
void hanoi( unsigned int n )
{
    /* Compute the solution by using binary representation */
    for ( int x = 1; x < (1 << n); ++x ) {
        printf( "Move from peg %d to peg %d.\n", 
            (x & (x-1)) % 3, ((x | (x-1)) + 1) % 3 );
    }
}
                                                                                
int main( void )
{
    hanoi( 5 );

    return 0;
}
