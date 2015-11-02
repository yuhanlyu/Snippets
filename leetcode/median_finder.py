# Median is the middle value in an ordered integer list. If the size of the 
# list is even, there is no middle value. So the median is the mean of the two 
# middle value.
# Design a data structure that supports the following two operations:
# void addNum(int num) - Add a integer number from the data stream to the data 
# structure.
# double findMedian() - Return the median of all elements so far.
# Time Complexity: O(lg n)
# Space Complexity: O(n)

from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = None, [], []
        self.i = 1

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.h[-self.i], -heappushpop(self.h[self.i], num * self.i))
        self.i *= -1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return (self.h[self.i][0] * self.i - self.h[-1][0]) / 2.0
