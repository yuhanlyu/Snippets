/* Write a program to find the n-th ugly number.
 * Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
 * For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 
 * ugly numbers.
 * Note that 1 is typically treated as an ugly number.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    var numbers = [1], indices = [0, 0, 0], factors = [2, 3, 5];
    for (var i = 0; i < n - 1; ++i) {
        var candidates = [], min_index = 0, min = Infinity;
        for (var j = 0; j < factors.length; ++j) {
            var new_value = numbers[indices[j]] * factors[j];
            candidates.push(new_value);
            if (new_value < min) {
                min_index = j;
                min = new_value;
            }
        }
        numbers.push(min);
        for (j = 0; j < factors.length; ++j)
            if (numbers[indices[j]] * factors[j] === min)
                ++indices[j];
    }
    return numbers[numbers.length - 1];
};
