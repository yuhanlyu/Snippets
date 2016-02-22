/* Given two words word1 and word2, find the minimum number of steps required 
 * to convert word1 to word2. (each operation is counted as 1 step.)
 * You have the following 3 operations permitted on a word:
 * a) Insert a character
 * b) Delete a character
 * c) Replace a character
 * Time Complexity: O(nm)
 * Space Complexity: O(m)
 */

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    var F = new Array(word2.length + 1);
    for (var i = 0; i < F.length; ++i)
        F[i] = i;
    for (i = 1; i <= word1.length; ++i) {
        var left_top = F[0];
        F[0] = i;
        for (var j = 1; j <= word2.length; ++j) {
            var tmp = F[j];
            if (word1.charAt(i - 1) === word2.charAt(j - 1))
                F[j] = left_top;
            else
                F[j] = 1 + Math.min(F[j], F[j - 1], left_top);
            left_top = tmp;
        }
    }
    return F[word2.length];
};
