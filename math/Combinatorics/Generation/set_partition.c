#include <stdio.h>

void SP(int n, int m, int p, int c[]);
void setpart2(int n, int c[]);
void part1(int n, int c[]);

int main(void)
{
    int c[50] = {0};
    //SP(16, 0, 0, c);
    //setpart2(16, c);
    //part1(16, c);
    return 0;
}

/* Generate set partitions
 * The following algorithm is from Jörg Arndt's paper
 * "Subset-lex: did we miss an order?"
 */
void part1(int n, int a[])
{
    int m[n + 1];
    a[0] = 1;
    ++a;
    for (int i = 0; i < n; ++i)
        m[i] = 1;
    int tr = 1;
    while (1) {
        int j = tr;
        if (a[j] < m[j]) {
            ++a[j];
            // a is a new partition
            continue;
        }
        int j1 = j + 1;
        if (j1 < n) {
            m[j1] = m[j] + 1;
            a[j1] = 1;
            tr = j1;
            // a is a new partition
            continue;
        }
        a[j] = 0;
        m[j] = m[j - 1];
        do {
            --j;
        } while (a[j] == 0);
        if (j < 0) break;
        if (a[j] == m[j]) m[j + 1] = m[j];
        --a[j];
        ++j;
        a[j] = 1;
        tr = j;
        // a is a new partition
    }
}

/* Generate set partitions
 * The following algorithm is from this paper
 *  B. Djokic, M. Miyakawa, S. Sekiguchi, I. Semba, I. Stojmenovic 
 * "A fast iterative algorithm for generating set partitions"
 * The Computer Journal Volume 32 Issue 3, June 1989 Pages 281-282 
 */
void setpart2(int n, int c[])
{
    int b[n], r = 1, j = 0, n1 = n - 1;
    c[1] = b[0] = 1;
    do {
        while (r < n1) {
            c[b[++j] = ++r] = 1;
        }
        for (int k = 1; k <= n - j; ++k) {
            c[n] = k;
            // c is a new partition
        }
        if (++c[r = b[j]] > b[j] - j)
            --j;
    } while (r != 1);
}

/* Generate set partitions
 * The following algorithm is from M. C. Er's paper
 * "A Fast Algorithm for Generating Set Partitions"
 * The Computer Journal (1988) 31 (3): 283-284.
 */
void SP(int n, int m, int p, int c[])
{
    if (p < n - 1) {
        for (int i = 1; i <= m; ++i) {
            c[p] = i;
            SP(n, m, p + 1, c);
        }
        c[p] = m + 1;
        SP(n, m + 1, p + 1, c);
    } else {
        for (int i = 1; i <= m + 1; ++i) {
            c[p] = i;
            // c is a new partition
        }
    }
}
