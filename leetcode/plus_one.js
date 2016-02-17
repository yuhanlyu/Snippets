/* Given a non-negative number represented as an array of digits, 
 * plus one to the number.
 * The digits are stored such that the most significant digit is at the 
 * head of the list.
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (var i = digits.length - 1; i >= 0; digits[i--] = 0) {
        if (digits[i] !== 9) {
            ++digits[i]
            return digits
        }
    }
    digits.unshift(1)
    return digits
};
