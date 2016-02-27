class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        steal, not_steal = 0, 0
        for num in A:
            steal, not_steal = not_steal + num, max(steal, not_steal)
        return max(steal, not_steal)
