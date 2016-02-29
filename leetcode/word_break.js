/* Given a string s and a dictionary of words dict, determine if s can be 
 * segmented into a space-separated sequence of one or more dictionary words.
 * Time Complexity: O(n^2 + m) in average, m is the size of dictionary
 * Space Complexity: O(n + m)
 */

/**
 * @param {string} s
 * @param {set<string>} wordDict
 *   Note: wordDict is a Set object, see:
 *   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    var trie = new Map();
    for (var word of wordDict) {
        var node = trie;
        for (var i = word.length - 1; i >= 0; --i) {
            var c = word.charAt(i);
            if (!node.has(c))
                node.set(c, new Map());
            node = node.get(c);
        }
        node.set(null, null);
    }
    var F = new Array(s.length + 1);
    F.fill(false);
    F[0] = true;
    for (i = 0; i < s.length; ++i) {
        node = trie;
        for (var j = i; !F[i + 1] || j >= 0; --j) {
            if (!node.has(s.charAt(j)))
                break;
            node = node.get(s.charAt(j));
            if (F[j] && node.has(null))
                F[i + 1] = true;
        }
    }
    return F[s.length];
};
