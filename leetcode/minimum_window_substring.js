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
        if (!need.has(c))
            need.set(c, 0);
        need.set(c, need.get(c) + 1);
    }
    var histogram = new Map(), remain = t.length;
    var begin = 0, end = s.length, cur = 0;
    for (var i = 0; i < s.length; ++i) {
        c = s.charAt(i);
        if (need.has(c)) {
            if (!histogram.has(c))
                histogram.set(c, 0);
            histogram.set(c, histogram.get(c) + 1);
            if (histogram.get(c) <= need.get(c))
                --remain;
        }
        for (; remain === 0; ++cur) {
            if (i - cur < end - begin) {
                begin = cur;
                end = i;
            }
            if (need.has(s.charAt(cur))) {
                histogram.set(s.charAt(cur), histogram.get(s.charAt(cur)) - 1);
                if (histogram.get(s.charAt(cur)) < need.get(s.charAt(cur)))
                    ++remain;
            }
        }
    }
    return end - begin < s.length ? s.substring(begin, end + 1) : "";
};
