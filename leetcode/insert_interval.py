# Given a set of non-overlapping intervals, insert a new interval into the 
# intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their 
# start times.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        start, end = newInterval.start, newInterval.end
        inserted, result = False, []
        for i in intervals:
            if i.start > newInterval.end:
                if not inserted: 
                    result.append(Interval(start, end))
                    inserted = True
                result.append(i)
            elif i.end < newInterval.start:
                result.append(i)
            else:
                start, end = min(start, i.start), max(end, i.end)
        if not inserted: result.append(Interval(start, end))
        return result

if __name__ == "__main__":
    solution = Solution()
    ints = solution.insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5))
    for int in ints:
        print int.start, int.end
    print 
    ints = solution.insert([Interval(1, 2), Interval(3, 5),
                            Interval(6, 7), Interval(8, 10),
                            Interval(12, 16)], Interval(4, 9))
    for int in ints:
        print int.start, int.end
    print 
