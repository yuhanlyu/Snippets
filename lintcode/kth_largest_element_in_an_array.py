class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        def search(k, left, right):
            pivot, begin, end = A[right], left, right
            while True:
                while A[left] < pivot and left < right:
                    left += 1
                while A[right] >= pivot and left < right:
                    right -= 1
                if left >= right:
                    break
                A[left], A[right] = A[right], A[left]
            A[left], A[end] = A[end], A[left]
            if k == (left - begin) + 1:
                return A[left]
            if k < (left - begin) + 1:
                return search(k, begin, left - 1)
            return search(k - (left - begin + 1), left + 1, end)
        return search(len(A) - k + 1, 0, len(A) - 1)
