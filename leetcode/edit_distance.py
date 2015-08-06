# Given two words word1 and word2, find the minimum number of steps required 
# to convert word1 to word2. (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# a) Insert a character
# b) Delete a character
# c) Replace a character
# Time Complexity: O(nm)
# Space Complexity: O(m)

class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        F = [i for i in xrange(len(word2) + 1)]
        for i in xrange(1, len(word1) + 1):
            left_top, F[0] = F[0], i
            for j in xrange(1, len(word2) + 1):
                left_top, F[j] = F[j], left_top if word1[i - 1] == word2[j - 1]\
                                       else 1 + min(F[j], F[j - 1], left_top)
        return F[-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.minDistance("kitten", "sitting")
    print solution.minDistance("Saturday", "Sunday")
