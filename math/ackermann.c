#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

/** 
 *Computing Ackermann function
 * The following algoirthm is from this paper:
 * Jerrold W. Grossman and R.Suzanne Zeitman
 * "An inherently iterative computation of ackermann's function,"
 * Theoretical Computer Science Volume 57, Issues 2–3, May 1988, Pages 327–330
 * Time complexity is O(mA(m, n)), space complexity is O(m)
 * There is another algorithm with tiem complexity O(A(m, n))
 * Yanhong A. Liu and Scott D. Stoller,
 * "Optimizing Ackermann's function by incrementalization,"
 * PEPM '03 Proceedings of the 2003 ACM SIGPLAN workshop on Partial 
 * evaluation and semantics-based program manipulation Pages 85 - 91 
 * But this algorithm is more complicated.
 * Since when m is large, the value of Ackermann function will be extremely 
 * large and is infeasible to compute within reasonable time, the difference 
 * between O(mA(m, n)) and O(A(m, n)) will be small in practice.
 */
int Ackermann(int m, int n);
int Ackermann(int m, int n)
{
    int next[m + 1], goal[m + 1], value, i;
    for (i = 0; i <= m; ++i) {
        next[i] = 0;
        goal[i] = 1;
    }
    for (goal[m] = -1; next[m] != n + 1; ++next[i]) {
        for (value = next[i = 0] + 1; next[i] == goal[i]; ++next[i++])
            goal[i] = value;
    }
    return value;
}

// Naive implementation
int AckermannRec( int m, int n );
int AckermannRec( int m, int n )
{
    if ( m == 0 )
        return n + 1;
    if ( n == 0 )
        return Ackermann( m - 1, 1 );
    return Ackermann( m - 1, Ackermann( m, n - 1 ) );
}

int main(void)
{
    for (int m = 0; m <= 3; ++m) {
        for (int n = 0; n < 5; ++n) {
            assert(Ackermann(m, n) == AckermannRec(m, n));
        }
    }
}
