/* Given a string s, partition s such that every substring of the partition is 
 * a palindrome.
 * Return all possible palindrome partitioning of s.
 */

/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    function helper(s, DP, index, cur, result) {
        if (index === s.length)
            result.push(cur.slice());
        else {
            for (var i = index; i < s.length; ++i) {
                if (DP[index][i]) {
                    cur.push(s.substring(index, i + 1));
                    helper(s, DP, i + 1, cur, result);
                    cur.pop();
                }
            }
        }
        return result;
    }
    var DP = new Array(s.length);
    for (var i = 0; i < s.length; ++i) {
        var temp = new Array(s.length);
        temp.fill(false);
        DP[i] = temp;
        DP[i][i] = true;
    }
    for (var k = 1; k < s.length; ++k) {
        for (i = 0; i < s.length - k; ++i) {
            if ((k === 1 || DP[i + 1][i + k - 1])
             && s.charAt(i) === s.charAt(i + k))
                DP[i][i + k] = true;
        }
    }
    return helper(s, DP, 0, [], []);
};
