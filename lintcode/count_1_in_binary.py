class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        num -= ((num >> 1) & 0x55555555)
        num = (num & 0x33333333) + ((num >> 2) & 0x33333333)
        return (((num + (num >> 4) & 0x0F0F0F0F) * 0x01010101) & 0xFFFFFFFF) >> 24
