class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        current = 0
        for index in xrange(len(A)):
            if A[index] != elem:
                A[current] = A[index]
                current += 1
        return current
