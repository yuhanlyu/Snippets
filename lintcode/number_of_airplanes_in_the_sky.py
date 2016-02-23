"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        P = []
        for interval in airplanes:
            P.extend([(interval.start, 1), (interval.end, 0)])
        P.sort()
        max, cur = 0, 0
        for p, t in P:
            if t == 1:
                cur += 1
                if cur > max:
                    max = cur
            elif t == 0:
                cur -= 1
        return max
