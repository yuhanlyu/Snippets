/* Returns the index of the first occurrence of needle in haystack, 
 * or -1 if needle is not part of haystack.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle === "")
        return 0
    var failure = [-1]
    for (var i = 1; i <= needle.length; ++i) {
        for (var pos = failure[i-1]; pos != -1 && needle[pos] !== needle[i-1];)
            pos = failure[pos]
        failure[i] = pos + 1
    }
    for (var ti = 0, pi = 0; ti < haystack.length; ++ti) {
        while (pi != -1 && haystack[ti] !== needle[pi])
            pi = failure[pi]
        if (++pi === needle.length)
            return ti + 1 - needle.length
    }
    return -1
};
