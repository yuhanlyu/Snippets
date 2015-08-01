# Given two strings s and t, write a function to determine if t is an anagram 
# of s.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        histogram = [0] * 26
        for c in s: histogram[ord(c) - ord('a')] += 1
        for c in t: histogram[ord(c) - ord('a')] -= 1
        return all(n == 0 for n in histogram)

if __name__ == "__main__":
    solution = Solution()
    print solution.isAnagram("anagram", "nagaram")
    print solution.isAnagram("rat", "car")
