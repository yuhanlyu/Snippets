# Given a collection of intervals, merge all overlapping intervals.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        result = []
        for i in sorted(intervals, key = lambda x: (x.start, x.end)):
            if result and i.start <= result[-1].end:
                result[-1].end = max(result[-1].end, i.end)
            else:
                result.append(i)
        return result

if __name__ == "__main__":
    solution = Solution()
    ints = solution.merge([Interval(1, 3), Interval(2, 6),
                           Interval(8, 10), Interval(15, 18)])
    for int in ints:
        print int.start, int.end
