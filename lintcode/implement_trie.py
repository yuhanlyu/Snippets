"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
    def __init__(self):
        self.map = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.map.setdefault(c, TrieNode())
        node.map[None] = None

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for c in word:
            if c in node.map:
                node = node.map[c]
            else: return False
        return None in node.map

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.map:
                node = node.map[c]
            else: return False
        return True
