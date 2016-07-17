#include "binary_search.h"

int32_t binary_search(int32_t A[], int32_t n, int32_t x) {
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

int32_t biased_search(int32_t A[], int32_t n, int32_t x) {
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
