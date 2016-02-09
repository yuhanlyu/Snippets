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
    for (i = 0; i < intervals.length; ++i) {
        if (result.length > 0 && intervals[i].start <= 
                                 result[result.length - 1].end)
            result[result.length - 1].end = Math.max(intervals[i].end,
                                            result[result.length - 1].end)
        else
            result.push(interval[i])
    }
    return result
};
