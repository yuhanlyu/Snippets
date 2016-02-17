/* Given a string, determine if it is a palindrome, considering only 
 * alphanumeric characters and ignoring cases.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    for (var left = 0, right = s.length - 1; left < right; ++left, --right) {
        while (left < right && !/^[a-z0-9]+$/i.test(s[left]))
            ++left
        while (left < right && !/^[a-z0-9]+$/i.test(s[right]))
            --right
        if (s[left].toLowerCase() !== s[right].toLowerCase())
            return false
    }    
    return true
};
