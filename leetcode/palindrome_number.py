# Determine whether an integer is a palindrome.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0): 
            return False
        rev_first_half = 0
        while rev_first_half < x:
            rev_first_half = 10 * rev_first_half + x % 10
            x /= 10
        return rev_first_half == x or rev_first_half / 10 == x

if __name__ == "__main__":
    solution = Solution()
    print solution.isPalindrome(1234321)
