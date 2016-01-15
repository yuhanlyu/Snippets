class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        current = 0
        for num in A:
            if current == 0 or num > A[current - 1]:
                A[current] = num
                current += 1
        return current 
