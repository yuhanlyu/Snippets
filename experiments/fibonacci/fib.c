#include "fib.h"

int64_t doubling(int32_t n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    int32_t j, nn = n;
    for (j = 0; nn > 0; nn >>= 1, ++j) ;
    int64_t s1 = 0, s2 = 1;
    for (int32_t k = j - 2; k >= 0; --k) {
        int64_t t = s2 * s2, s2k = s1 * s1 + t, s2k1 = t + ((s1 * s2) << 1);
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

int64_t tumble(int32_t n) {
    int64_t even = 0, odd = 1;
    int32_t i;

    // even is the i-th fibonacci number
    // odd is the (i+1)-th fibonacci number
    for (i = 0; i < n; i += 2) {
        odd += even;
        even += odd;
    }
    return i == n ? even : odd;
}

int64_t iterative(int32_t n) {
    int64_t first = 0, second = 1;
    while (n-- > 0) {
        int64_t t = first + second;
        first = second;
        second = t;
    }
    return first;
}

int64_t qmatrix(int32_t n) {
    int64_t a = 1, b = 0, c = 0, d = 1;
    for (--n; n > 0; n >>= 1) {
        if (n & 1) {
            int64_t t = d * (b + a) + c * b;
            a = d * b + c * a;
            b = t;
        }
        int64_t t = d *((c << 1) + d);
        c = c * c + d * d;
        d = t;
    }
    return a + b;
}
