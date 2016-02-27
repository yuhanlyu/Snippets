class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        pivot = len(num) - 1
        while pivot > 0 and num[pivot - 1] >= num[pivot]:
            pivot = pivot - 1
        if pivot == 0:
            num.reverse()
        else:
            n, index = num[pivot - 1], len(num) - 1
            while num[index] <= n:
                index = index - 1
            num[index], num[pivot - 1] = num[pivot - 1], num[index]
            for i in xrange((len(num) - pivot) / 2):
                num[pivot + i], num[~i] = num[~i], num[pivot + i]
        return num
