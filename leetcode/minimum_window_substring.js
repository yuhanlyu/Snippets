/* Given a string S and a string T, find the minimum window in S which will 
 * contain all the characters in T in complexity O(n).
 * Time Complexity: O(n) in average
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    var need = new Map();
    for (var c of t.split("")) {
        if (!(c in need))
            need[c] = 0;
        ++need[c];
    }
    var histogram = new Map(), remain = t.length;
    var begin = 0, end = s.length, cur = 0;
    for (var i = 0; i < s.length; ++i) {
        c = s.charAt(i);
        if (c in need) {
            if (!(c in histogram))
                histogram[c] = 0;
            if (++histogram[c] <= need[c])
                --remain;
        }
        for (; remain === 0; ++cur) {
            if (i - cur < end - begin) {
                begin = cur;
                end = i;
            }
            if (s.charAt(cur) in need 
            && --histogram[s.charAt(cur)] < need[s.charAt(cur)])
                    ++remain;
        }
    }
    return end - begin < s.length ? s.substring(begin, end + 1) : "";
};
