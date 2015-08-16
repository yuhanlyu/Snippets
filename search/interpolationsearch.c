int InterpolationSearch( int a[], int n, int key )
{
	int		left = 0, right = n - 1, middle;

	while ( left <= right ) {
		middle = ( ( key - a[ left ] ) / ( a[ right ] - a[ left ] ) )
				 * ( right - left ) + left;
		if ( key == a[ middle ] )
			return middle;
		if ( key > a[ middle ] )
			left = middle + 1;
		else
			right = middle - 1;
	}
	return -1;
}
