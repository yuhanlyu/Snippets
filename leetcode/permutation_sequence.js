/* Given n and k, return the kth permutation sequence.
 * Time Complexity: O(n^2)
 * Space Complexity: O(n), assuming rotation in place
 */

/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    var result = [], fac = 1;
    for (var i = 0; i < n; ++i) {
        result.push(i + 1);
        if (i > 1)
            fac *= i;
    }
    for (--k, i = 0; i < n - 1; ++i) {
        var d = Math.floor(k / fac);
        k -= fac * d;
        if (d > 0) {
            var tmp = result[i + d];
            for (var j = i + d; j > i; --j)
                result[j] = result[j - 1];
            result[i] = tmp;
        }
        fac = Math.floor(fac / (n - 1 - i));
    }
    return result.join("");
};
