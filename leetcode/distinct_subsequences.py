# Given a string S and a string T, count the number of distinct subsequences 
# of T in S.
# A subsequence of a string is a new string which is formed from the original 
# string by deleting some (can be none) of the characters without disturbing 
# the relative positions of the remaining characters. (ie, "ACE" is a 
# subsequence of "ABCDE" while "AEC" is not).
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        F = [0] * (len(t) + 1)
        F[0] = 1
        for i in xrange(1, len(s) + 1):
            for j in xrange(min(i, len(t)), 0, -1):
                F[j] += F[j - 1] if t[j - 1] == s[i - 1] else 0
        return F[-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.numDistinct("rabbbit", "rabbit")
