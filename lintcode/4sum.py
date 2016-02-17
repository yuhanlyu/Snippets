class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self, numbers, target):
        unique = set()
        numbers.sort()
        for i in xrange(len(numbers) - 3):
            for j in xrange(i + 1, len(numbers) - 2):
                k = numbers[i] + numbers[j]
                left, right = j + 1, len(numbers) - 1
                while left < right:
                    s = k + numbers[left] + numbers[right]
                    if s == target:
                        unique.add((numbers[i], numbers[j], numbers[left], numbers[right]))
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return [list(x) for x in unique]
