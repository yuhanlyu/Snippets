#include "binary_search.h"

int32_t binary_search(const int32_t A[], int32_t n, int32_t x) {
    int32_t low = 0;
    for (int32_t high = n - 1; low <= high; ) {
        int32_t mid = low + ((high - low) >> 1);
        if (A[mid] >= x)
            high = mid - 1;
        else
            low = mid + 1;
    } 
    return low;
}

int32_t biased_search(const int32_t A[], int32_t n, int32_t x) {
    int32_t low = 0;
    for (int32_t high = n - 1; low <= high; ) {
        int32_t mid = low + ((high - low) >> 2);
        if (A[mid] >= x)
            high = mid - 1;
        else
            low = mid + 1;
    } 
    return low;
}

int32_t size_specialized_search(const int32_t A[], int32_t n, int32_t x) {
    const int32_t* base = A;
    for (n >>= 1; n > 0; n >>= 1) {
        const int32_t* mid = base + n;
        if (*mid <= x)
            base = mid;
    }
    return base - A;
}
