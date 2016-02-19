class Solution:
    """
    @param A : An integer array
    @return : An integer
    """
    def singleNumberII(self, A):
        one, two = 0, 0
        for num in A:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        return one
