# Given an input string, reverse the string word by word.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

if __name__ == "__main__":
    solution = Solution()
    print solution.reverseWords("  a  b  cd  ")
