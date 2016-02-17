/* Given n non-negative integers representing an elevation map where the width 
 * of each bar is 1, compute how much water it is able to trap after raining.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    var result = 0
    for (var h = 0, left = 0, right = height.length - 1; left <= right; ) {
        h = Math.max(h, Math.min(height[left], height[right]))
        if (height[left] < height[right]) {
            if (height[left] < h)
                result += h - height[left]
            ++left
        } else {
            if (height[right] < h)
                result += h - height[right]
            --right
        }
    }
    return result
};
