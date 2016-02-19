/* Given an integer array of size n, find all elements that appear more than n/3
 * times.
 * Time complexity: O(n) in average
 * Space complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    var K = new Map();
    for (var num of nums) {
        if (!(num in K))
            K.set(num, 0);
        K.set(num, K.get(num) + 1);
        if (K.length >= 3) {
            for (var item of K) {
                K.set(num, K.get(num) - 1);
                if (K.get(num) === 0)
                    K.delete(num);
            }
        }
    }
    var result = [];
    for (var candidate of K) {
        var count = 0;
        for (num of nums)
            if (num === candidate[0])
                ++count;
        if (count > Math.floor(nums.length / 3))
            result.push(candidate[0]);
    }
    return result;
};
