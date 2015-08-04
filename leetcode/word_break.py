# Given a string s and a dictionary of words dict, determine if s can be 
# segmented into a space-separated sequence of one or more dictionary words.
# Time Complexity: O(n^2 + m) in average, m is the size of dictionary
# Space Complexity: O(n + m)

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        trie = {}
        for word in wordDict:
            node = trie
            for c in word[::-1]:
                node = node.setdefault(c, {})
            node[None] = None
        F = [False] * (len(s) + 1)
        F[0] = True
        for i in xrange(len(s)):
            j, node = i, trie
            while not F[i + 1] or j >= 0:
                if s[j] not in node: break
                node = node[s[j]]
                if F[j] and None in node: F[i + 1] = True
                j -= 1
        return F[len(s)]
                

if __name__ == "__main__":
    solution = Solution()
    print solution.wordBreak("leetcode", ["leet", "code"])
