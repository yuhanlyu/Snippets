/* Given two integers n and k, return all possible combinations of k numbers 
 * out of 1 ... n.
 * Time Complexity: O(n^k)
 * Space Complexity: O(n^k)
 */

/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    var result = [];
    for (var x = (1 << k) - 1; x < (1 << n); ) {
        var temp = [];
        for (var i = 0; i < n; ++i)
            if ((x >> i) & 1)
                temp.push(i + 1);
        result.push(temp);
        u = x & -x;
        v = u + x;
        x = v | (((v^x) / u) >> 2);
    }
    return result;
};
