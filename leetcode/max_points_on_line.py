# Given n points on a 2D plane, find the maximum number of points that lie on 
# the same straight line.
# Time Complexity: O(n^2) in average
# Space Complexity: O(n)

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from fractions import Fraction, gcd

class Solution:
    # @param {Point[]} points
    # @return {integer}
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

if __name__ == "__main__":
    solution = Solution()
    print solution.maxPoints([Point(0, 0), Point(0, 0)])
