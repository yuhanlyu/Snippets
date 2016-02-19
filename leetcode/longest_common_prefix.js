/* Write a function to find the longest common prefix string amongst 
 * an array of strings.
 * Time Complexity: O(n)
 * Space Complexity: O(output)
 */

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0)
        return "";
    for (var i = 0; ; ++i) {
        for (var str of strs) {
            if (i >= str.length || str.charAt(i) !== strs[0].charAt(i))
                return strs[0].substring(0, i);
        }
    }
};
