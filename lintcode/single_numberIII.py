class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        xor, ans = 0, 0
        for num in A:
            xor ^= num
        for num in A:
            if xor & -xor & num:
                ans ^= num
        return [xor ^ ans, ans]
