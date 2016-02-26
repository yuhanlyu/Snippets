# class Comparator:
#     def cmp(self, a, b)
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        def helper(left, right):
            if left >= right:
                return
            pivot = partition(nuts, left, right, lambda a : compare.cmp(a, bolts[right]))
            partition(bolts, left, right, lambda b : -compare.cmp(nuts[pivot], b))
            helper(left, pivot - 1)
            helper(pivot + 1, right)
        def partition(arr, left, right, cmp):
            j = left
            while j < right:
                if cmp(arr[j]) == 0:
                    arr[j], arr[right] = arr[right], arr[j]
                    j -= 1
                elif cmp(arr[j]) < 0:
                    arr[left], arr[j] = arr[j], arr[left]
                    left += 1
                j += 1
            arr[left], arr[right] = arr[right], arr[left]
            return left
        helper(0, len(nuts) - 1)
