# Given a string s consists of upper/lower-case alphabets and empty space 
# characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Time Complexity: O(n)
# Space Compelxtity : O(1)

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        length, start = 0, False
        for index in xrange(len(s) - 1, -1, -1):
            if s[index] == ' ':
                if start: break
            else:
                length += 1
                start = True
        return length
                
if __name__ == "__main__":
    solution = Solution()
    print solution.lengthOfLastWord("Hello World")
