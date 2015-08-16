void Shaker( int a[], int n )
{
    int     i, left = 1, right = n, flag, tmp;
                                                                                
    do {
        for ( flag = 0, i = left; i < right; ++i )
            if ( a[ i - 1 ] > a[ i ] ) {
                tmp = a[ i - 1 ];
                a[ i - 1 ] = a[ i ];
                a[ i ] = tmp;
                flag = 1;
            }
        --right;
                                                                                
        if ( flag == 0 )
            break;
                                                                                
        for ( flag = 0, i = right - 1; i >= left; --i )
            if ( a[ i - 1 ] > a[ i ] ) {
                tmp = a[ i - 1 ];
                a[ i - 1 ] = a[ i ];
                i[ i ] = tmp;
                flag = 1;
		}
		--right;

		if ( flag == 0 )
            break;
                                                                                
        for ( flag = 0, i = right - 1; i >= left; --i )
            if ( a[ i - 1 ] > a[ i ] ) {
                tmp = a[ i - 1 ];
                a[ i - 1 ] = a[ i ];
                a[ i ] = tmp;
                flag = 1;
            }
        ++left;
    } while ( flag == 1 );
}
