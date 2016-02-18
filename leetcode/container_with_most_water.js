/* Given n non-negative integers a1, a2, ..., an, where each represents a point 
 * at coordinate (i, ai). n vertical lines are drawn such that the two 
 * endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together 
 * with x-axis forms a container, such that the container contains the most 
 * water.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var result = 0;
    for (left = 0, right = height.length - 1; left < right; ) {
        result = Math.max(result, (right - left) * 
                                  Math.min(height[left], height[right]));
        if (height[left] < height[right])
            ++left;
        else
            --right
    }
    return result
};
