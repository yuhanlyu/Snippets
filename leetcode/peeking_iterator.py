# Given an Iterator class interface with methods: next() and hasNext(), 
# design and implement a PeekingIterator that support the peek() operation -- 
# it essentially peek() at the element that will be returned by the next call 
# to next().

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.cache = iterator.next() if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator
        :rtype: int
        """
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        temp = self.cache
        self.cache = self.iter.next() if self.iter.hasNext() else None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cache is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
