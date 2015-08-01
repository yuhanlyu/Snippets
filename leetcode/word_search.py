# Design a data structure that supports the following two operations:
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string 
# containing only letters a-z or .. A . means it can represent any one letter.
# Time Complexity: O(n)
# Space Complexity: O(n)

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[None] = None

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        l = [self.root]
        for c in word:
            l = [x for node in l for k, x in node.items() 
                 if c in (k, ".") and x]
        return any(None in node for node in l)

if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    print wordDictionary.search("pattern")
    print wordDictionary.search("word")
    print wordDictionary.search("wo.xx")
