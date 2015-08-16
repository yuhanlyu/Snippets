void bSelection( int a[], int n )
{
    int     left, right, i, min, max, tmp;
                                                                                
    for ( left = 0, right = n - 1; left < right; ++left, --right ) {
                                                                                
        if ( n % 2 ) {
            min = max = left;
            i = left + 1;
        } else {
            if ( a[ left ] > a[ left + 1 ] ) {
                max = left;
                min = left + 1;
            } else {
                max = left + 1;
                min = left;
            }
            i = left + 2;
        }
                                                                                
        for ( ; i < right; i += 2 ) {
            if ( a[ i ] > a[ i + 1 ] ) {
                if ( a[ i ] > a[ max ] )
                    max = i;
                if ( a[ i + 1 ] < a[ min ] )
                    min = i + 1;
            } else {
                if ( a[ i + 1 ] > a[ max ] )
                    max = i + 1;
                if ( a[ i ] < a[ min ] )
                    min = i;
            }
        }
                                                                                
        tmp = a[ min ];
        a[ min ] = a[ left ];
        a[ left ] = tmp;
                                                                                
        if ( max == left ) {
            tmp = a[ min ];
            a[ min ] = a[ right ];
            a[ right ] = tmp;
        } else {
            tmp = a[ max ];
            a[ max ] = a[ right ];
            a[ right ] = tmp;
        }
    }
}
