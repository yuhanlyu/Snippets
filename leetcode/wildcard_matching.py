# Implement wildcard pattern matching with support for '?' and '*'.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        i, j, match, star = 0, 0, 0, -1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i, j = i + 1, j + 1
            elif j < len(p) and p[j] == '*':
                star, match, j = j + 1, i + 1, j + 1
            elif star >= 0:
                i, j, match = match, star, match + 1
            else: return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

if __name__ == "__main__":
    solution = Solution()
    print solution.isMatch("aa","a")
    print solution.isMatch("aa","aa")
    print solution.isMatch("aaa","aa")
    print solution.isMatch("aa", "*")
    print solution.isMatch("aa", "a*")
    print solution.isMatch("ab", "?*")
    print solution.isMatch("aab", "c*a*b")
