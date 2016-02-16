/* Given n points on a 2D plane, find the maximum number of points that lie on 
 * the same straight line.
 * Time Complexity: O(n^2) in average
 * Space Complexity: O(n)
 */

/**
 * Definition for a point.
 * function Point(x, y) {
 *     this.x = x;
 *     this.y = y;
 * }
 */
/**
 * @param {Point[]} points
 * @return {number}
 */
var maxPoints = function(points) {
    function gcd(a, b) {
        while ((a %= b) && (b %= a))
            ;
        return a + b
    }
    for (var result = 0, i = 0; i < points.length; ++i) {
        dict = {}
        for (var count = 0, j = 0; j < points.length; ++j) {
            var dx = points[j].x - points[i].x
            var dy = points[j].y - points[i].y
            if (dx == 0 && dy == 0)
                ++count
            else {
                var d = gcd(dx, dy)
                dx /= d
                dy /= d
            }
            var m = dx != 0 ? [dy, dx] : null
            if (m in dict)
                dict[m] = dict[m] + 1
            else
                dict[m] = 1
        }
        dict[null] -= count
        for(var key in dict) {
            if(count + dict[key] > result)
                result = count + dict[key]
        }
    }
    return result
};
