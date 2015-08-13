#include <stdio.h>

// Using Qmatrix method to compute fibonacci number
unsigned int qmatrix(unsigned int n);
unsigned int qmatrix(unsigned int n)
{
    unsigned int a = 1, b = 0, c = 0, d = 1;
    for (--n; n > 0; n >>= 1) {
        if (n & 1){
            unsigned int t = d * (b + a) + c * b;
            a = d * b + c * a;
            b = t;
        }
        unsigned int t = d *((c << 1) + d);
        c = c * c + d * d;
        d = t;
    }
    return a + b;
}


int main( void )
{
    printf( "F20 should be 6765. fibonacci( 20 ) = %u\n", qmatrix(20) );
    printf( "F31 should be 1346269. fibonacci( 31 ) = %u\n", qmatrix(31) );

    return 0;
}
