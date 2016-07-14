#include "rotation.h"

static inline unsigned gcd(unsigned a, unsigned b);
static inline unsigned gcd(unsigned a, unsigned b) {
    while ((a %= b) && (b %= a))
        ;
    return a + b;
}

void juggling_bentley(unsigned A[], unsigned n, unsigned k) {
    for (unsigned i = 0, bound = gcd(n, k); i < bound; ++i) {
        unsigned to = i, from = (i + k) % n, temp = A[i];
        do {
            A[to] = A[from];
            to = from;
            from = (from + k) % n;
        } while (from != i);
        A[to] = temp;
    }
}

void juggling_shene(unsigned A[], unsigned n, unsigned k) {
    for (unsigned i = 0, bound = n; i < bound; ++i) {
        unsigned to = i, from = (i + k) % n, temp = A[i];
        do {
            A[to] = A[from];
            to = from;
            if (from < bound)
                bound = from;
            from = (from + k) % n;
        } while (from != i);
        A[to] = temp;
    }
}

static inline void reverse(unsigned A[], unsigned l, unsigned r);
static inline void reverse(unsigned A[], unsigned l, unsigned r) {
    while (l < r) {
        unsigned temp = A[l];
        A[l++] = A[r];
        A[r--] = temp;
    }
}

void rotate_reverse(unsigned A[], unsigned n, unsigned k) {
    reverse(A, 0, k - 1);
    reverse(A, k, n - 1);
    reverse(A, 0, n - 1);
}

void block_swap_shene(unsigned A[], unsigned n, unsigned k) {
    for (unsigned left = 0, right = k, middle = k; ;) {
        unsigned temp = A[left];
        A[left++] = A[right];
        A[right++] = temp;
        if (left == middle) {
            if (right == n)
                return;
            middle = right;
        } else if (right == n)
            right = middle;
    }
}

static inline void swap_section(unsigned A[], unsigned i, 
                                unsigned j, unsigned k);
static inline void swap_section(unsigned A[], unsigned i, 
                                unsigned j, unsigned k) {
    while (k-- > 0) {
        unsigned temp = A[i];
        A[i++] = A[j];
        A[j++] = temp;
    }
}

void block_swap_gries(unsigned A[], unsigned n, unsigned k) {
    unsigned i = k;
    for (unsigned j = n - k; i != j; ) {
        if (i > j) {
            swap_section(A, k - i, k, j);
            i -= j;
        } else {
            swap_section(A, k - i, k + j - i, i);
            j -= i;
        }
    }
    swap_section(A, k - i, k, i);
}
