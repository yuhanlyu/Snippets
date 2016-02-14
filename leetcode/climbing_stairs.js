/* You are climbing a stair case. It takes n steps to reach to the top.
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can 
 * you climb to the top?
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)
 */
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    for (var x = 1, y = 0, a = 1, b = 1; n > 0; n >>= 1) {
        if (n & 1) {
            t = a * x + b * y
            y = b * x + y * (a - b)
            x = t
        }
        t = a * a + b * b
        b *= 2 * a - b
        a = t
    }
    return x   
};
