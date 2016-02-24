class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        b, result = {}, 0
        for n in num:
            if n not in b:
                left, right = b.get(n - 1, n), b.get(n + 1, n)
                result = max(result, right - left + 1)
                b[n], b[left], b[right] = n, right, left
        return result
