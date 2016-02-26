class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        def sift_down(k):
            while k < len(A):
                min = k
                if k * 2 + 1 < len(A) and A[k * 2 + 1] < A[min]:
                    min = k * 2 + 1
                if k * 2 + 2 < len(A) and A[k * 2 + 2] < A[min]:
                    min = k * 2 + 2
                if min == k:
                    return
                A[min], A[k] = A[k], A[min]
                k = min

        for i in range(len(A) / 2, -1, -1):
            sift_down(i)
