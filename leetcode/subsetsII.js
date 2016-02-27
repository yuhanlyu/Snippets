/* Given a collection of integers that might contain duplicates, nums, 
 * return all possible subsets.
 * Time Complexity: O(n2^n)
 * Space Complexity: O(n2^n)
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    var cnt = new Map();
    for (var num of nums) {
        if (!cnt.get(num))
            cnt.set(num, 0);
        cnt.set(num, cnt.get(num) + 1);
    }
    var c = new Array(cnt.size);
    c.fill(0);
    nums = Array.from(cnt.keys());
    nums.sort(function(a, b) { return a - b; });
    for (var result = []; true; ) {
        for (var tmp = [], i = 0; i < c.length; ++i) {
            if (c[i] > 0) {
                var t = new Array(c[i]);
                t.fill(nums[i]);
                tmp.push(t);
            }
        }
        result.push([].concat.apply([], tmp));
        for (var j = 0; j < nums.length && c[j] === cnt.get(nums[j]); ++j)
            c[j] = 0;
        if (j === nums.length)
            break;
        ++c[j];
    }
    return result;
};
