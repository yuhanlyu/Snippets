/* Given a collection of numbers that might contain duplicates, 
 * return all possible unique permutations.
 * Time Complexity: O((n+1)!)
 * Space Complexity: O((n+1)!)
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    nums.sort();
    for (var result = [nums.slice()]; true; ) {
        for (var i = nums.length - 2; i >= 0 && nums[i] >= nums[i + 1]; --i)
            ;
        if (i < 0)
            break;
        for (var j = nums.length - 1; nums[i] >= nums[j]; --j)
            ;
        var temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        nums = nums.slice(0, i + 1).concat(nums.slice(i + 1).reverse());
        result.push(nums.slice());
    }
    return result;
};
