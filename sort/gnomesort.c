void GnomeSort( int a[], int n )
{
	int		i, tmp;

	for ( i = 0; i < n; )
		if ( i == 0 || a[ i - 1 ] <= a[ i ] )
			++i;
		else {
			tmp = a[ i ];
			a[ i ] = a[ i - 1 ];
			a[ --i ] = tmp;
		}
}
