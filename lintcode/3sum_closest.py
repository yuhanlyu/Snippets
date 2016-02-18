class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        numbers.sort()
        result = numbers[0] + numbers[1] + numbers[2]
        for index in xrange(len(numbers) - 2):
            left, right = index + 1, len(numbers) - 1
            while left < right:
                sum = numbers[index] + numbers[left] + numbers[right]
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return result
