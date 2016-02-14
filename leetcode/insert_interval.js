/* Given a set of non-overlapping intervals, insert a new interval into the 
 * intervals (merge if necessary).
 * You may assume that the intervals were initially sorted according to their 
 * start times.
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
 * @param {Interval} newInterval
 * @return {Interval[]}
 */
var insert = function(intervals, newInterval) {
    var start = newInterval.start
    var end = newInterval.end
    var inserted = false;
    var result = []
    for (var i = 0; i < intervals.length; ++i) {
        if (intervals[i].start > newInterval.end) {
            if (!inserted) {
                result.push(new Interval(start, end))
                inserted = true
            }
            result.push(intervals[i])
        } else if (intervals[i].end < newInterval.start)
            result.push(intervals[i])
        else {
            start = Math.min(start, intervals[i].start)
            end = Math.max(end, intervals[i].end)
        }
    }
    if (!inserted)
        result.push(new Interval(start, end))
    return result
};
