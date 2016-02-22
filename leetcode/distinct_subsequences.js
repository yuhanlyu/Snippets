/* Given a string S and a string T, count the number of distinct subsequences 
 * of T in S.
 * A subsequence of a string is a new string which is formed from the original 
 * string by deleting some (can be none) of the characters without disturbing 
 * the relative positions of the remaining characters. (ie, "ACE" is a 
 * subsequence of "ABCDE" while "AEC" is not).
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    var F = new Array(t.length + 1);
    F.fill(0)
    F[0] = 1
    for (var i = 1; i <= s.length; ++i) {
        for (var j = Math.min(i, t.length); j > 0; --j) {
            if (t.charAt(j - 1) === s.charAt(i - 1))
                F[j] += F[j - 1];
        }
    }
    return F[t.length];
};
