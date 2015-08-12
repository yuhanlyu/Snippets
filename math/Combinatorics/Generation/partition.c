#include <stdio.h>

void partitionASC(int n);
void partitionDSC(int n);
int main(void)
{
    return 0;
}

/* Generating Integer Partitions
 * Ascending representation is faster
 * The following algorithm is from this paper
 * Jerome Kelleher Barry O'Sullivan, 
 *  "Generating All Partitions: A Comparison Of Two Encodings"
 */
void partitionASC(int n)
{
    int a[n];
    a[0] = 0, a[n - 1] = n;
    for (int k = 1; k != 0;) {
        int x = a[k - 1] + 1, y;
        for (y = a[k--] - 1; x <= y; y -= x)
            a[k++] = x;
        a[k] = x + y;
        // a[] is a new partition 
    }
}

void partitionDSC(int n)
{
    int d[n];
    d[n - 1] = n;
    for (int k = 0; k != n - 1; ){
        int l = k, m, nn;
        for (m = d[k]; m == 1; m = d[--k]) ;
        for (nn = m-- + l - k; m < nn; nn -= m)
            d[k++] = m;
        d[k] = nn;
        // a[] is a new partition 
    }
}
