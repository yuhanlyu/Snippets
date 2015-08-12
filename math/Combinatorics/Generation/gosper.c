#include <stdio.h>

int main(void)
{
    unsigned k = 15, N = 30;
    for (unsigned comb = (1 << k) - 1; comb < 1 << N;) {
        unsigned x = comb & -comb, y = comb + x;
        comb = ((comb & ~y) / x >> 1) | y;
    }
    return 0;
}
