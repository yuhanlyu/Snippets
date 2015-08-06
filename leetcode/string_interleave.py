# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
# Time Complexity: O(nm) in average
# Space Complexity: O(n)

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        L = [0]
        for i in xrange(len(s3)):
            s = set((j for j in L if i - j < len(s2) and s2[i - j] == s3[i]))
            s.update((j+1 for j in L if j < len(s1) and s1[j] == s3[i]))
            L = list(s)
        return len(s1) in L

if __name__ == "__main__":
    solution = Solution()
    print solution.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print solution.isInterleave("aabcc", "dbbca", "aadbbbaccc")
