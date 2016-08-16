#ifndef JOSEPHUS_H_
#define JOSEPHUS_H_

#include <cstdint>

// O(n) algorithm
// D. Woodhouse, "Programming the Josephus problem,"
// ACM SIGCSE Bulletin, Volume 10 Issue 4, December 1978 Pages 56-58
int32_t woodhousea(int32_t n, int32_t m);

// Concrete Mathematics 3.3
int32_t concrete_math(int64_t n, int32_t m);

// Method from TAOCP 1.3.3 Exercise 31
// O(log_{m/(m-1)} n(m-1))
int32_t taocp(int32_t n, int32_t m);

// Method from TAOCP
int32_t taocp_k(int32_t n, int32_t m, int32_t k);

// Fatih Gelgi's method in "Time Improvement on Josephus Problem"
// I modified the recursive algorithm in the paper to be a iterative one.
// O(m + lg_{m/(m-1)} (n/m))
int32_t gelgi(int32_t n, int32_t m);

// My space-efficient version of Gelgi's method
int32_t gelgi_improve(int32_t n, int32_t m);

#endif
