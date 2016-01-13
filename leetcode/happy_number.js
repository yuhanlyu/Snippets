/* Write an algorithm to determine if a number is "happy".
 * A happy number is a number defined by the following process: 
 * Starting with any positive integer, replace the number by the sum of the 
 * squares of its digits, and repeat the process until the number equals 1 
 * (where it will stay), or it loops endlessly in a cycle which does not 
 * include 1. Those numbers for which this process ends in 1 are happy numbers.
 * Space Complexity: O(1)
 */

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    function sumOfSquare(n) {
        for (var result = 0; n > 0; n = Math.floor(n / 10)) {
            var remainder = n % 10
            result += remainder * remainder
        }
        return result
    }
    var slow = sumOfSquare(n), fast = sumOfSquare(sumOfSquare(n))
    while (slow != fast) {
        slow = sumOfSquare(slow)
        fast = sumOfSquare(sumOfSquare(fast))
    }
    return fast == 1 ? true : false
};
