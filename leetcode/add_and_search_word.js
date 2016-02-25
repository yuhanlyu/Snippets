/* Design a data structure that supports the following two operations:
 * void addWord(word)
 * bool search(word)
 * search(word) can search a literal word or a regular expression string 
 * containing only letters a-z or .. A . means it can represent any one letter.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @constructor
 */
var WordDictionary = function() {
    this.root = new Map();
};

/**
 * @param {string} word
 * @return {void}
 * Adds a word into the data structure.
 */
WordDictionary.prototype.addWord = function(word) {
    var node = this.root;
    for (var c of word) {
        if (!node.get(c))
            node.set(c, new Map());
        node = node.get(c);
    }
    node.set(null, null);
};

/**
 * @param {string} word
 * @return {boolean}
 * Returns if the word is in the data structure. A word could
 * contain the dot character '.' to represent any one letter.
 */
WordDictionary.prototype.search = function(word) {
    var l = [this.root];
    for (var c of word) {
        var temp = [];
        for (var node of l) {
            if (node.get(c)) {
                temp.push(node.get(c));
            } else if (c === '.') {
                for (var entry of node) {
                    if (entry[0] !== null)
                        temp.push(entry[1]);
                }
            }
        }
        l = temp;
    }
    for (node of l) {
        if (node.get(null) === null)
            return true;
    }
    return false;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var wordDictionary = new WordDictionary();
 * wordDictionary.addWord("word");
 * wordDictionary.search("pattern");
 */
