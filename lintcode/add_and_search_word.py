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


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
