int LinearSearch( int a[], int n, int key )
{
	int		i, tmp = a[ n - 1 ];

	for ( a[ n - 1 ] = key, i = 0; a[ i ] != key; ++i )
		;
	return i != n - 1 ? i :
		   tmp == key ? n - 1 : -1;
}
