class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def countOfSmallerNumberII(self, A):
        def sort(enum):
            mid = len(enum) / 2
            if mid:
                left, right = sort(enum[:mid]), sort(enum[mid:])
                for i in xrange(len(enum) - 1, -1, -1):
                    if not left or right and right[-1][1] > left[-1][1]:
                        smaller[right[-1][0]] += len(left)
                        enum[i] = right.pop()
                    else:
                        enum[i] = left.pop()
            return enum
        smaller = [0] * len(A)
        sort(list(enumerate(A)))
        return smaller
