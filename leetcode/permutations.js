/* Given a collection of numbers, return all possible permutations.
 * Time Complexity: O((n+1)!)
 * Space Complexity: O((n+1)!)
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var c = new Array(nums.length);
    c.fill(0);
    for (var result = [nums.slice()], i = 1; i < nums.length; ) {
        if (c[i] === i) {
            c[i] = 0;
            ++i;
        } else {
            var temp = nums[i];
            nums[i] = nums[(i % 2) * c[i]];
            nums[(i % 2) * c[i]] = temp;
            result.push(nums.slice());
            ++c[i];
            i = 1;
        }
    }
    return result;
};
