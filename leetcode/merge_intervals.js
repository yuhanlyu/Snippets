/* Given a collection of intervals, merge all overlapping intervals.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function(intervals) {
    result = []
    intervals.sort(function(a, b) {
        if (a.start != b.start)
            return a.start - b.start
        return a.end - b.end
    })
    for (var interval of intervals) {
        if (result.length > 0 && interval.start <= result[result.length - 1].end)
            result[result.length - 1].end = Math.max(interval.end,
                                            result[result.length - 1].end)
        else
            result.push(interval)
    }
    return result
};
