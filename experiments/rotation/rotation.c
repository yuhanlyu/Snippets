#include "rotation.h"

static inline int32_t gcd(int32_t a, int32_t b);
static inline int32_t gcd(int32_t a, int32_t b) {
    while ((a %= b) && (b %= a))
        ;
    return a + b;
}

void juggling_bentley(int32_t A[], int32_t n, int32_t k) {
    for (int32_t i = 0, bound = gcd(n, k); i < bound; ++i) {
        int32_t to = i, from = (i + k) % n, temp = A[i];
        do {
            A[to] = A[from];
            to = from;
            from = (from + k) % n;
        } while (from != i);
        A[to] = temp;
    }
}

void juggling_shene(int32_t A[], int32_t n, int32_t k) {
    for (int32_t i = 0, bound = n; i < bound; ++i) {
        int32_t to = i, from = (i + k) % n, temp = A[i];
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

static inline void reverse(int32_t A[], int32_t l, int32_t r);
static inline void reverse(int32_t A[], int32_t l, int32_t r) {
    while (l < r) {
        int32_t temp = A[l];
        A[l++] = A[r];
        A[r--] = temp;
    }
}

void rotate_reverse(int32_t A[], int32_t n, int32_t k) {
    reverse(A, 0, k - 1);
    reverse(A, k, n - 1);
    reverse(A, 0, n - 1);
}

void block_swap_shene(int32_t A[], int32_t n, int32_t k) {
    int32_t count = 0;
    for (int32_t left = 0, right = k, middle = k; ;) {
        int32_t temp = A[left];
        A[left++] = A[right];
        A[right++] = temp;
        ++count;
        if (left == middle) {
            if (right == n)
                return;
            middle = right;
        } else if (right == n)
            right = middle;
    }
}

static inline void swap_section(int32_t A[], int32_t i, int32_t j, int32_t k);
static inline void swap_section(int32_t A[], int32_t i, int32_t j, int32_t k) {
    while (k-- > 0) {
        int32_t temp = A[i];
        A[i++] = A[j];
        A[j++] = temp;
    }
}

void block_swap_gries(int32_t A[], int32_t n, int32_t k) {
    int32_t i = k;
    for (int32_t j = n - k; i != j; ) {
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
