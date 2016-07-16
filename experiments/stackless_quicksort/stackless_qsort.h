#ifndef STACKLESS_QSORT_H_
#define STACKLESS_QSORT_H_

#include <stdint.h>

// Stackless quicksort: 
//    sort the array A[2..end - 1), assuming A[0], A[1], and A[end]
//    are modifiable.
//
// This algorithm is from Lutz M. Wegner's paper
// "A generalized, one-way, stackless quicksort,"
// BIT Numerical Mathematics 1987, Volume 27, Issue 1, pp 44-48
void stackless_qsort(int32_t A[], int32_t end);

// For example:
//
// int32_t A[size + 1];
// stackless_qsort(A, size) will sort the A[2]..A[size - 1] (inclusively),
// assuming that A[0], A[1] and A[size] are modifiable.
// The effect is the same as std::sort(A + 2, A + size);

#endif
