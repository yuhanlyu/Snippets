#include <stdio.h>
#include <math.h>

int main( void )
{
    double  pi, t = 1.0;
    int     i;

    /* pi = 4 - 4/3 + 4/5 - 4/7 + 4/9...... */
    for ( pi = 0.0, i = 1; fabs( pi - t ) > 0.000001; i += 2 ) {
        t = pi;
        if ( i % 4 == 3 )
            pi -= 4.0 / i;
        else
            pi += 4.0 / i;
    }

    printf( "%f\n", pi );

    return 0;
}

