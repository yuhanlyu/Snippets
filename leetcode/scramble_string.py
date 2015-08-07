# Given a string s1, we may represent it as a binary tree by partitioning it 
# to two non-empty substrings recursively.
# Time Complexity: O(n^4)
# Space Complexity: O(n^3)

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        L = [[set([j for j in xrange(len(s2)) if s1[i] == s2[j]])
                     for i in xrange(len(s1))]]
        for k in xrange(1, len(s1)):
            L.append([])
            for i in xrange(len(s1) - k):
                L[-1].append(set())
                for m in xrange(k):
                    for j in L[m][i]:
                        if j + m + 1 in L[k - m - 1][i + m + 1]: 
                            L[-1][-1].add(j)
                        if j - k + m in L[k - m - 1][i + m + 1]:
                            L[-1][-1].add(j - k + m)
        return len(L[-1][-1]) > 0

if __name__ == "__main__":
    solution = Solution()
    print solution.isScramble("rgeat", "great")
    print solution.isScramble("rgtae", "great")
