void shellsort( int a[], int n )
{
	int		i, j, h, tmp;

	for ( h = 1; h <= n / 9; h = 3 * h + 1 )
		;
	for ( ; h > 0; h /= 3 )
		for ( i = h; i < n; ++i ) {
			for ( tmp = a[ j = i ]; j >= h && a[ j - h ] > tmp; j -= h )
				a[ j ] = a[ j - h ];
			a[ j ] = tmp;
		}
}
