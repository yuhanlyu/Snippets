class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        if not L: return 0
        left, right = 1, max(L)
        while left <= right:
            mid = left + (right - left) / 2
            if sum([x / mid for x in L]) < k:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
