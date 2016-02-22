/* Given a string S, find the longest palindromic substring in S. 
 * You may assume that the maximum length of S is 1000, and 
 * there exists one unique longest palindromic substring.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    var T = ["^"].concat(s.split(""), "$").join("#");
    var P = new Array(T.length), C = 0, R = 0, max = 0, center = 0;
    P.fill(0);
    for (var i = 1; i < T.length - 1; ++i) {
        P[i] = R >= i ? Math.min(R - i, P[2 * C - i]) : 1;
        while (T[i + 1 + P[i]] === T[i - 1 - P[i]])
            ++P[i];
        if (P[i] > max) {
            max = P[i];
            center = i;
        }
        if (i + P[i] > R) {
            C = i;
            R = P[i] + i
        }
    }
    return s.substring(Math.floor((center - max)/2), Math.floor((center + max)/2));
};
