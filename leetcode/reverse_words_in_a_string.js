/* Given an input string, reverse the string word by word.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string} str
 * @returns {string}
 */
var reverseWords = function(str) {
    return str.split(" ").filter(function(a) {return a.length > 0})
                         .reverse().join(" ")
};
