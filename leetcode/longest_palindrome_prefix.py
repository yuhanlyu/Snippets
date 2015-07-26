# Given a string S, you are allowed to convert it to a palindrome by adding 
# characters in front of it. Find and return the shortest palindrome you can 
# find by performing this transformation.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        t, F = s + "#" + s[::-1], [0] * (len(s) * 2 + 1)
        for index in xrange(1, len(t)):
            pos = F[index - 1]
            while pos > 0 and t[pos] != t[index]:
                pos = F[pos - 1]
            F[index] = pos if t[pos] != t[index] else pos + 1
        return s[-1:-1 - len(s) + F[-1]:-1] + s

if __name__ == "__main__":
    solution = Solution()
    print solution.shortestPalindrome("aacecaaa")
    print solution.shortestPalindrome("abcd")
