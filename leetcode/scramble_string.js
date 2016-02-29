/* Given a string s1, we may represent it as a binary tree by partitioning it 
 * to two non-empty substrings recursively.
 * Time Complexity: O(n^4) in average
 * Space Complexity: O(n^3)
 */

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var isScramble = function(s1, s2) {
    var L = [];
    for (var i = 0; i < s1.length; ++i) {
        var t = new Set();
        for (var j = 0; j < s2.length; ++j) {
            if (s1.charAt(i) === s2.charAt(j))
                t.add(j);
        }
        L.push(t);
    }
    L = [L];
    for (var k = 1; k < s1.length; ++k) {
        t = [];
        for (i = 0; i < s1.length - k; ++i)
            t.push(new Set());
        L.push(t);
        for (i = 0; i < s1.length - k; ++i) {
            for (var m = 0; m < k; ++m) {
                for (j of L[m][i]) {
                    if (L[k-m-1][i+m+1].has(j + m + 1))
                        L[k][i].add(j);
                    if (L[k-m-1][i+m+1].has(j + m - k))
                        L[k][i].add(j + m - k);
                }
            }
        }
    }
    L = L[L.length - 1];
    return L[L.length - 1].size > 0;
};
