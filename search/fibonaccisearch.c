int FibonacciSearch( int a[], int n, int key )
{
	int root, d1, d2, tmp;

	for ( tmp = 1; fibonacci( tmp ) <= n; ++tmp )
		;
	root = fibonacci( tmp - 1);
	d1 = fibonacci( tmp - 2 );
	d2 = root - d1;

	do {
		if ( key == a[ root - 1 ] )
			return root - 1;
		else if ( key < a[ root - 1 ] ) {
			root -= d2;
			tmp = d1;
			d1 = d2;
			d2 = tmp - d2;
		} else {
			root += d2;
			d1 -= d2;
			d2 -= d1;
		}
	} while ( d2 >= 0 );
	return -1;
}
