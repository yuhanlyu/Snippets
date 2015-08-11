#include <stdio.h>

/** Computes the solution of tower of Hanoi for given numberOfDisks */
void hanoi( unsigned int numberOfDisks );
void hanoi( unsigned int numberOfDisks )
{
    /* Compute the solution by using binary representation */
    for ( int x = 1; x < (1 << numberOfDisks); ++x ) {
        printf( "Move from peg %d to peg %d.\n", 
            (x & (x-1)) % 3, ((x | (x-1)) + 1) % 3 );
    }
}
                                                                                
int main( void )
{
    hanoi( 5 );

    return 0;
}
