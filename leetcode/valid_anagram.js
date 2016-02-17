/* Given two strings s and t, write a function to determine if t is an anagram 
 * of s.
 * Time Complexity: O(n lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length)
        return false
    s = s.split("").sort()
    t = t.split("").sort()
    for (var i = 0; i < s.length; ++i)
        if (s[i] !== t[i])
            return false
    return true
};
