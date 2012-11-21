#include <stdio.h>
#include <limits.h>

/* Print the binary representation of integer num */
void intBitPrint( int num );
void intBitPrint( int num )
{
    for ( int i = sizeof( num ) * CHAR_BIT; i >= 0; --i ) {
        putchar( num & ( 1 << i ) ? '1' : '0' );
    }
    puts( "" );
}

int main( void )
{
    puts( "Binary representation of 50 should be 000000000000000000000000000110010" );
    printf( "bit_print( 50 ) = " );
    intBitPrint( 50 );
    return 0;
}
