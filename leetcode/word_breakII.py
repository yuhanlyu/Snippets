# Given a string s and a dictionary of words dict, add spaces in s to construct
# a sentence where each word is a valid dictionary word.
# Return all such possible sentences.

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        def helper(s, i, neighbors, cur, result):
            if i == len(s): result.append(' '.join(cur))
            else:
                for neighbor in neighbors.get(i, []):
                    helper(s, neighbor, neighbors, cur+[s[i:neighbor]], result)
            return result
        trie, neighbors = {}, {}
        for word in wordDict:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node[None] = None
        found = False
        for i in xrange(len(s)):
            j, node = i, trie
            while node and j < len(s):
                if s[j] not in node: break
                node = node[s[j]]
                if None in node: 
                    neighbors.setdefault(i, []).append(j + 1)
                    if j + 1 == len(s): found = True
                j += 1
        return helper(s, 0, neighbors, [], []) if found else []

if __name__ == "__main__":
    solution = Solution()
    print solution.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])
