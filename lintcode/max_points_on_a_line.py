# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from fractions import gcd
class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        result = 0
        for p1 in points:
            dict, count = {}, 0
            for p2 in points:
                dx, dy = p2.x - p1.x, p2.y - p1.y
                if dx == 0 == dy: count += 1
                else: dy, dx = dy / gcd(dx, dy), dx / gcd(dx, dy)
                m = (dy, dx) if dx else None
                dict[m] = dict.get(m, 0) + 1
            dict[None] -= count
            result = max(result, count + max(dict.viewvalues()))
        return result
