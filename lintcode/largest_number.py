class Solution: 
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        return ''.join(sorted([str(n) for n in num], cmp=lambda x, y: cmp(y+x, x+y))).lstrip('0') or '0'
