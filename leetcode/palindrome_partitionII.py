# Given a string s, partition s such that every substring of the partition is 
# a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        F, P = [-1] * (len(s) + 1), []
        for i in xrange(len(s)):
            P = [begin - 1 for begin in P if begin > 0 and s[begin - 1] == s[i]]
            if i > 0 and s[i - 1] == s[i]: P.append(i - 1)
            P.append(i)
            F[i + 1] = 1 + min(F[j] for j in P)
        return F[-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.minCut("aab")
