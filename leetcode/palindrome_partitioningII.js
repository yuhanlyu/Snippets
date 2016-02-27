/* Given a string s, partition s such that every substring of the partition is 
 * a palindrome.
 * Return the minimum cuts needed for a palindrome partitioning of s.
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @return {number}
 */
var minCut = function(s) {
    var F = new Array(s.length + 1);
    F.fill(-1);
    for (var P = [], i = 0; i < s.length; ++i) {
        var t = [];
        for (var begin of P)
            if (begin > 0 && s.charAt(begin - 1) === s.charAt(i))
                t.push(begin - 1);
        P = t;
        if (i > 0 && s.charAt(i - 1) === s.charAt(i))
            P.push(i - 1);
        P.push(i);
        F[i + 1] = s.length;
        for (var j of P)
            if (F[j] + 1 < F[i + 1])
                F[i + 1] = F[j] + 1;
    }
    return F[s.length];
};
