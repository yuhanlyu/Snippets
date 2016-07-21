#ifndef BINARY_SEARCH_H_
#define BINARY_SEARCH_H_

#include <stdint.h>

// Find the index of leftmost insertion x in a sorted array 
// with length n > 0.
int32_t binary_search(const int32_t A[], int32_t n, int32_t x);

// Biased binary search.
// This algorithm is from the following paper:
// Gerth Stølting Brodal, Gabriel Moruz,Skewed Binary Search Trees,
// Lecture Notes in Computer Science Volume 4168, 2006, pp 708-719
int32_t biased_search(const int32_t A[], int32_t n, int32_t x);

// Size-specialized binary search.
// The length of A must be power of two.
int32_t size_specialized_search(const int A[], int32_t n, int32_t x);

#endif
