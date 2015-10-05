# Given a pattern and a string str, find if str follows the same pattern.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return len(set(zip(str.split(), pattern)))  \
            == len(set(str.split())) == len(set(pattern))

if __name__ == "__main__":
    solution = Solution()
    print solution.wordPattern("abba", "dog cat cat dog")
    print solution.wordPattern("abba", "dog cat cat fish")
    print solution.wordPattern("aaaa", "dog cat cat dog")
    print solution.wordPattern("abba", "dog dog dog dog")
