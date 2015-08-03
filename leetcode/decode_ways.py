# A message containing letters from A-Z is being encoded to numbers using the 
# following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of 
# ways to decode it.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s or s[0] == "0": return 0
        cur, before = 1, 1
        for i in xrange(1, len(s)):
            t = int(s[i - 1: i + 1])
            if s[i] == '0': cur = 0
            cur, before = cur + (before if 10 <= t <= 26 else 0), cur
        return cur

if __name__ == "__main__":
    solution = Solution()
    print solution.numDecodings("27")
    print solution.numDecodings("0")
