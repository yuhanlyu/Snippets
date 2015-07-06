# Given a string, determine if it is a palindrome, considering only 
# alphanumeric characters and ignoring cases.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print solution.isPalindrome("A man, a plan, a canal: Panama")
    print solution.isPalindrome("race a car")
