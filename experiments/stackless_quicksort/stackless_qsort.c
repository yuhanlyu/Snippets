#include "stackless_qsort.h"

#include <limits.h>

void stackless_qsort(int32_t A[], int32_t end) {
    A[1] = A[end] = INT32_MIN;
    for (int32_t left = 2; left <= end;) {
        // A[left] is a stopper
        if (A[left] <= A[left - 1]) {
            A[left - 2] = A[left];
            left += 2;
            continue;
        }
        int32_t i = left, j = left;
        for (int32_t pivot = A[left]; ; A[j] = A[++i]) {
            // Find the next out of order position
            while (pivot < A[++j]) ;

            // A[j] is a stopeer, partition the current part is finished
            if (A[j] <= A[left - 1]) {
                A[i] = pivot;
                break;
            }

            // A[j] is not a stopper
            if (A[j] >= A[i - 1]) {
                A[i] = A[j]; // A[i] must be the maximum of the left part
            } else {
                A[i] = A[i - 1];
                A[i - 1] = A[j];
            }
        }
        if (left + 2 >= i) {
            A[left - 2] = A[j];
            A[j] = A[i - 1];
            left = i + 1;
        } else {
            int32_t temp = A[i - 1];
            A[i - 1] = A[j];
            A[j] = temp;
        }
    }
}
