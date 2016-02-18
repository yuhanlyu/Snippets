/* Given a string, find the length of the longest substring without repeating 
 * characters. For example, the longest substring without repeating letters 
 * for "abcabcbb" is "abc", which the length is 3. 
 * For "bbbbb" the longest substring is "b", with the length of 1.
 * Time Complexity: O(n) in average
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var max_length = 0, last = {};
    for (var begin = 0, i = 0; i < s.length; ++i ) {
        if (s[i] in last && begin < last[s[i]] + 1)
            begin = last[s[i]] + 1;
        else
            max_length = Math.max(max_length, i - begin + 1);
        last[s[i]] = i;    
    }
    return max_length;
};
