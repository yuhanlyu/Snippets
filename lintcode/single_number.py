class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        return reduce(lambda a, b: a ^ b, A) if A else 0
