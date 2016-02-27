class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer
    """
    def kSumII(self, A, k, target):
        def helper(start, cur, need, result):
            if len(cur) == k:
                if need == 0:
                    result.append(list(cur))
            else:
                for i in xrange(start, len(A)):
                    if need / (k - len(cur)) >= A[i]:
                        helper(i + 1, cur + [A[i]], need - A[i], result)
            return result
        A.sort()
        return helper(0, [], target, [])
