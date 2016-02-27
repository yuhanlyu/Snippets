/* Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
 * Time Complexity: O(nm)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    if (s1.length + s2.length !== s3.length)
        return false;
    for (var L = [0], i = 0; i < s3.length; ++i) {
        var LL = [];
        for (var j of L) {
            if (i - j < s2.length && s2.charAt(i - j) === s3.charAt(i) 
             && (LL.length === 0 || LL[LL.length - 1] !== j))
                LL.push(j);
            if (j < s1.length && s1.charAt(j) === s3.charAt(i))
                LL.push(j + 1);
        }
        L = LL;
    }
    return L.indexOf(s1.length) !== -1;
};
