#include <stdio.h>
#include <ctype.h>

int main( void )
{
    int     blank_cnt = 0, digit_cnt = 0, c;
    int     letter_cnt = 0, nl_cnt = 0, other_cnt = 0;

    while ( ( c = getchar() ) != EOF )
        if ( c == ' ' )
            ++blank_cnt;
        else if ( isdigit( c ) )
            ++digit_cnt;
        else if ( isalpha( c ) )
            ++letter_cnt;
        else if ( c == '\n' )
            ++nl_cnt;
        else
            ++other_cnt;

    printf("%d %d %d %d %d",blank_cnt,digit_cnt, letter_cnt, nl_cnt, other_cnt);
    return 0;
}

