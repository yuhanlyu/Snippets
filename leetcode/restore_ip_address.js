/* Given a string containing only digits, restore it by returning all possible 
 * valid IP address combinations.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    if (s.length === 0 || s.length > 12)
        return [];
    var DP1 = new Array(s.length);
    for (var i = 0; i < DP1.length; ++i)
        DP1[i] = [];
    for (i = 0; i < s.length; ++i) {
        DP1[i] = [s.charAt(i)];
        if (s[i] !== '0' && i + 2 <= s.length)
            DP1[i].push(s.substring(i, i + 2));
        if (s[i] !== '0' && i + 3 <= s.length && parseInt(s.substring(i, i + 3)) <= 255)
            DP1[i].push(s.substring(i, i + 3));
    }
    var DP2 = [];
    for (i = 0; i < s.length; ++i) {
        var tmp = [];
        for (var p of DP1[i]) {
            if (i + p.length === s.length)
                continue;
            for (var q of DP1[i + p.length])
                tmp.push([p, q]);
        }
        DP2.push(tmp);
    }
    var result = [];
    for (p of DP2[0]) {
        var prefix = p.join("");
        if (prefix.length === s.length)
            continue;
        for (q of DP2[prefix.length]) {
            var suffix = q.join("");
            if (prefix.length + suffix.length !== s.length)
                continue;
            result.push(p.concat(q).join("."));
        }
    }
    return result;
};
