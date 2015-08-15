#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>

/* Computing Ackermann function
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
 */
int Ackermann(int m, int n);
int Ackermann(int m, int n)
{
    int next[m + 1], goal[m + 1], value;
    for (int i = 0; i <= m; ++i) {
        next[i] = 0;
        goal[i] = 1;
    }
    goal[m] = -1;
    do {
        value = next[0] + 1;
        int transfer = 1;
        for (int i = 0; transfer; ++i) {
            if (next[i] == goal[i]) {
                goal[i] = value;
            } else {
                transfer = 0;
            }
            ++next[i];
        }
    } while (next[m] != n + 1);
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
