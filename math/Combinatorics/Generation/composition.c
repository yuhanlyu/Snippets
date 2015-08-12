#include <stdio.h>

/* Generate all integer compositions
 * The following algorithm is from this paper:
 * Toufik Mansour and Ghalib Nassar
 * "Loop-Free Gray Code Algorithms for the Set of Compositions"
 * Journal of Mathematical Modelling and Algorithms December 2010, 
 * Volume 9, Issue 4, pp 343-356
 */
int main(void)
{
    int a[100], n = 6;
    a[1] = 1, a[2] = n - 1;
    // [n] is a composition
    for (int pos = 1; pos > 0; ) {
        // a is a composition
        if (a[pos + 1] > 1) {
            ++pos;
            a[pos + 1] = a[pos] - 1;
            a[pos] = 1;
        } else {
            if (--pos > 0) {
                ++a[pos];
                a[pos + 2] -= 1;
            }
        }
    }
    return 0;
}
