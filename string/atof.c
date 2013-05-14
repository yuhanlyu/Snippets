#include <stdio.h>
#include <ctype.h>

/* Converting a string to a floating point number 
 * When str is NULL or does not contain any valid sequence, return 0.0 
 * This function stasfies the requirement of C90.
 * In C99 and C11, valid sequence contains 0x prefix, INF, and NAN, but
 * we didn't deal with these cases.
 */
double atof( const char str[] );
double atof( const char str[] )
{
    if ( str == NULL )
        return 0.0;
    /* Discard the heading whitespaces */
    for ( ; isspace( *str ); ++str )
        ;
    int sign = ( *str == '-' ) ? -1 : 1;
    if ( *str == '-' || *str == '+' )
        ++str;
    /* If there is no valid sequence, return 0.0 */
    if ( !isdigit( *str ) )
        return 0.0;
    double val;
    for ( val = 0.0; isdigit( *str ); ++str )
        val = 10.0 * val + ( *str - '0' );

    /* Fraction */
    if ( *str == '.' )
        ++str;
    double power;
    for ( power = 1.0; isdigit( *str ); ++str ) {
        val = 10.0 * val + ( *str - '0' );
        power *= 10.0;
    }
    val = sign * val / power;

    /* Exponent */
    if ( *str == 'e' || *str == 'E' ) {
        ++str;
        sign = ( *str == '-' ? -1 : 1 );
        if ( *str == '+' || *str == '-' )
            ++str;
        double exp;
        for ( exp = 0; isdigit( *str ); ++str )
            exp = 10 * exp + ( *str - '0' );
        if ( sign == 1 )
            while ( exp-- > 0 )
                val *= 10.0;
        else
            while ( exp-- > 0 )
                val /= 10.0;
    }
    return val;
}

int main( void )
{
    printf( "%f\n", atof( "1.2" ) );
    printf( "%f\n", atof( "-3.4" ) );
    printf( "%f\n", atof( "+5.6e7" ) );
    printf( "%f\n", atof( "-8.9e10" ) );
    printf( "%f\n", atof( "1.1e-2" ) );
    printf( "%f\n", atof( "+9.9e+10" ) );
    printf( "%f\n", atof( "+9.9ea" ) );
    printf( "%f\n", atof( "+9.9bc" ) );
    printf( "%f\n", atof( "1..2c" ) );
    printf( "%f\n", atof( NULL ) );
    printf( "%f\n", atof( "" ) );
    printf( "%f\n", atof( " abc" ) );
    return 0;
}
