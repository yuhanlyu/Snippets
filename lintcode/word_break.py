class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        trie = {}
        for word in dict:
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
