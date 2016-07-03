#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <time.h>

#define TEST_LENGTH 1000000U
#define TEST_CASES  100U 

unsigned gcd(unsigned a, unsigned b);
unsigned gcd(unsigned a, unsigned b) {
    while ((a %= b) && (b %= a))
        ;
    return a + b;
}

// Rotate an array circularly to the left by k positions
// This algorithm is from Jon Bentley's Programming Pearls.
void juggling_bentley(unsigned A[], unsigned n, unsigned k);
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

// Rotate an array circularly to the left by k positions
// This algorithm is from
// Ching-Kuang Shene, 
// An Analysis of Two In-Place Array Rotation Algorithms
// The Computer Journal (1997) 40 (9): 541-546.
void juggling_shene(unsigned A[], unsigned n, unsigned k);
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

void reverse(unsigned A[], unsigned l, unsigned r);
void reverse(unsigned A[], unsigned l, unsigned r) {
    while (l < r) {
        unsigned temp = A[l];
        A[l++] = A[r];
        A[r--] = temp;
    }
}

// Rotate an array circularly to the left by k positions
// This algorithm is from Jon Bentley's Programming Pearls.
void rotate_reverse(unsigned A[], unsigned n, unsigned k);
void rotate_reverse(unsigned A[], unsigned n, unsigned k) {
    reverse(A, 0, k - 1);
    reverse(A, k, n - 1);
    reverse(A, 0, n - 1);
}

// Rotate an array circularly to the left by k positions
// This algorithm is from
// Ching-Kuang Shene, 
// An Analysis of Two In-Place Array Rotation Algorithms
// The Computer Journal (1997) 40 (9): 541-546.
void block_swap_shene(unsigned A[], unsigned n, unsigned k);
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

void swap_section(unsigned A[], unsigned i, unsigned j, unsigned k);
void swap_section(unsigned A[], unsigned i, unsigned j, unsigned k) {
    while (k-- > 0) {
        unsigned temp = A[i];
        A[i++] = A[j];
        A[j++] = temp;
    }
}

// Rotate an array circularly to the left by k positions
// This algorithm is from
// David Gries and Harlan Mills,
// Swapping sections. 
// Technical Report TR 81-452, Cornell University.
void block_swap_gries(unsigned A[], unsigned n, unsigned k);
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

void time_used(struct timeval *t);
void time_used(struct timeval *t)
{
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    *t = ru.ru_utime;
}

int main(void)
{
    unsigned test[TEST_LENGTH] = {0};
    unsigned temp[TEST_LENGTH] = {0};
    unsigned shift[TEST_CASES] = {0};
    srand(time(NULL));
    for (unsigned int i = 0; i < TEST_LENGTH; ++i)
        test[i] = i;
    for (unsigned i = 0; i < TEST_CASES; ++i) {
        shift[i] = rand() % TEST_LENGTH;
    }

    struct timeval t0, t1, t2, t3, t4, t5, dt;
    time_used(&t0);
    for (unsigned i = 0; i < TEST_CASES; ++i)
        juggling_bentley(temp, TEST_LENGTH, shift[i]); 
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("Bentley's juggling algorithm used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned i = 0; i < TEST_CASES; ++i)
        juggling_shene(temp, TEST_LENGTH, shift[i]); 
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("Shene's juggling algorithm used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned i = 0; i < TEST_CASES; ++i)
        rotate_reverse(temp, TEST_LENGTH, shift[i]); 
    time_used(&t3);
    timersub(&t3, &t2, &dt);
    printf("Rotate by reversal algorithm used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned i = 0; i < TEST_CASES; ++i)
        block_swap_shene(temp, TEST_LENGTH, shift[i]); 
    time_used(&t4);
    timersub(&t4, &t3, &dt);
    printf("Shene's rotate by block swapping algorithm used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned i = 0; i < TEST_CASES; ++i)
        block_swap_gries(temp, TEST_LENGTH, shift[i]); 
    time_used(&t5);
    timersub(&t5, &t4, &dt);
    printf("Gries-Mills's rotate by block swapping algorithm used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
/*
    for (unsigned i = 0; i < TEST_CASES; ++i) {
        shift[i] = rand() % TEST_LENGTH;
        memcpy(temp, test, TEST_LENGTH * sizeof(int));
        juggling_bentley(temp, TEST_LENGTH, shift[i]); 
        for (unsigned j = 0; j < TEST_LENGTH; ++j)
            assert(temp[i] == (i + shift[i]) % TEST_LENGTH);
        memcpy(temp, test, TEST_LENGTH * sizeof(int));
        juggling_shene(temp, TEST_LENGTH, shift[i]); 
        for (unsigned j = 0; j < TEST_LENGTH; ++j)
            assert(temp[i] == (i + shift[i]) % TEST_LENGTH);
        memcpy(temp, test, TEST_LENGTH * sizeof(int));
        rotate_reverse(temp, TEST_LENGTH, shift[i]); 
        for (unsigned j = 0; j < TEST_LENGTH; ++j)
            assert(temp[i] == (i + shift[i]) % TEST_LENGTH);
        memcpy(temp, test, TEST_LENGTH * sizeof(int));
        block_swap(temp, TEST_LENGTH, shift[i]); 
        for (unsigned j = 0; j < TEST_LENGTH; ++j)
            assert(temp[i] == (i + shift[i]) % TEST_LENGTH);
        memcpy(temp, test, TEST_LENGTH * sizeof(int));
        block_swap_gries(temp, TEST_LENGTH, shift[i]); 
        for (unsigned j = 0; j < TEST_LENGTH; ++j)
            assert(temp[i] == (i + shift[i]) % TEST_LENGTH);
    }
*/
    return 0;
}
