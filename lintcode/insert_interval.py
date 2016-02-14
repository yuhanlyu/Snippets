"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
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
