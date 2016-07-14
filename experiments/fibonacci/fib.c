#include "fib.h"

unsigned doubling(unsigned n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    unsigned j, nn = n;
    for (j = 0; nn > 0; nn >>= 1, ++j) ;
    unsigned s1 = 0, s2 = 1;
    for (int k = j - 2; k >= 0; --k) {
        unsigned t = s2 * s2, s2k = s1 * s1 + t, s2k1 = t + ((s1 * s2) << 1);
        if ((n >> k) & 1) {
            s1 = s2k1;
            s2 = s2k + s2k1;
        } else {
            s1 = s2k;
            s2 = s2k1;
        }
    }
    return s2;
}

unsigned tumble(unsigned n) {
    unsigned even = 0, odd = 1, i;

    // even is the i-th fibonacci number
    // odd is the (i+1)-th fibonacci number
    for (i = 0; i < n; i += 2) {
        odd += even;
        even += odd;
    }
    return i == n ? even : odd;
}

unsigned iterative(unsigned n) {
    unsigned first = 0, second = 1;
    for (unsigned k = 0; k < n; ++k) {
        unsigned t = first + second;
        first = second;
        second = t;
    }
    return first;
}

unsigned qmatrix(unsigned n) {
    unsigned a = 1, b = 0, c = 0, d = 1;
    for (--n; n > 0; n >>= 1) {
        if (n & 1) {
            unsigned t = d * (b + a) + c * b;
            a = d * b + c * a;
            b = t;
        }
        unsigned t = d *((c << 1) + d);
        c = c * c + d * d;
        d = t;
    }
    return a + b;
}
