/* Implement a trie with insert, search, and startsWith methods.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @constructor
 * Initialize your data structure here.
 */
var TrieNode = function() {
    this.map = new Map();
};

var Trie = function() {
    this.root = new TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 * Inserts a word into the trie.
 */
Trie.prototype.insert = function(word) {
    var node = this.root;
    if (!node)
        return false;
    for (var c of word) {
        if (!(c in node.map))
            node.map[c] = new TrieNode();
        node = node.map[c];
    }
    node.map[null] = null;
};

/**
 * @param {string} word
 * @return {boolean}
 * Returns if the word is in the trie.
 */
Trie.prototype.search = function(word) {
    var node = this.root;
    for (var c of word) {
        if (c in node.map)
            node = node.map[c];
        else
            return false;
    }
    return null in node.map;
};

/**
 * @param {string} prefix
 * @return {boolean}
 * Returns if there is any word in the trie
 * that starts with the given prefix.
 */
Trie.prototype.startsWith = function(prefix) {
    var node = this.root;
    for (var c of prefix) {
        if (c in node.map)
            node = node.map[c];
        else
            return false;
    }
    return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var trie = new Trie();
 * trie.insert("somestring");
 * trie.search("key");
 */
