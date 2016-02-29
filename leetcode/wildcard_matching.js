/* Implement wildcard pattern matching with support for '?' and '*'.
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
 */

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    for (var i = 0, j = 0, match = 0, star = -1; i < s.length; ) {
        if (j < p.length && (p.charAt(j) === '?' || s.charAt(i) === p.charAt(j))) {
            ++i;
            ++j;
        } else if (j < p.length && p.charAt(j) === '*') {
            star = ++j;
            match = i + 1;
        } else if (star >= 0) {
            i = match++;
            j = star;
        } else {
            return false;
        }
    }
    for (; j < p.length && p.charAt(j) === '*'; ++j)
        ;
    return j === p.length;
};
