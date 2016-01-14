class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        m, n = len(A) - 1, len(B) - 1
        ans = [0] * (m + n + 2)
        while m >= 0 and n >= 0:
            if A[m] >= B[n]:
                ans[m + n + 1] = A[m]
                m -= 1
            else:
                ans[m + n + 1] = B[n]
                n -= 1
        if m >= 0:
            ans[:m + 1] = A[:m + 1]
        if n >= 0:
            ans[:n + 1] = B[:n + 1]
        return ans

solution = Solution()
print solution.mergeSortedArray([1], [1])
