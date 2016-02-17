/* A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
 * the diagram below).
 * The robot can only move either down or right at any point in time. The robot 
 * is trying to reach the bottom-right corner of the grid (marked 'Finish' in 
 * the diagram below).
 * How many possible unique paths are there?
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    var t = n
    n = Math.min(m - 1, n - 1)
    m = m + t - 2
    for (var result = 1, d = 1; d < n + 1; ++d) {
        result = Math.floor((result * m) / d)
        --m;
    }
    return result
};
