# Implement a trie with insert, search, and startsWith methods.
# Time Complexity: O(n)
# Space Complexity: O(n)

class TrieNode:
    # Initialize your data structure here.
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
            if c not in node.map:
                node.map[c] = TrieNode()
            node = node.map[c]
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

if __name__ == "__main__":
    trie = Trie()
    trie.insert("somestring")
    print trie.search("key")
    trie.insert("key")
    print trie.search("key")
    print trie.startsWith("some")
    print trie.startsWith("somet")
