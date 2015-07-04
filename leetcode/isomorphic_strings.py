# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character 
# while preserving the order of characters. No two characters may map to the 
# same character but a character may map to itself.
# Time Complexity: O(n)
# Space Complexity: O(sigma), the size of the alphabet

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapping, mapped = [None] * 256, [False] * 256
        for c1, c2 in zip(s, t):
            c1, c2 = ord(c1), ord(c2)
            if mapping[c1] is None and not mapped[c2]: 
                mapping[c1], mapped[c2] = c2, True
            elif mapping[c1] != c2:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print solution.isIsomorphic("egg", "add")
    print solution.isIsomorphic("foo", "bar")
    print solution.isIsomorphic("paper", "title")
