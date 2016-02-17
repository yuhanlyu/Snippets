class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        result = []
        numbers.sort()
        for index in xrange(len(numbers) - 2):
            if index == 0 or numbers[index] != numbers[index-1]:
                left, right = index + 1, len(numbers) - 1
                while left < right:
                    if numbers[index] + numbers[left] + numbers[right] == 0:
                        result.append([numbers[index], numbers[left], numbers[right]])
                        while left < right and numbers[left] == result[-1][1]:
                            left += 1
                        while left < right and numbers[right] == result[-1][2]:
                            right -= 1
                    elif numbers[index] + numbers[left] + numbers[right] < 0:
                        left += 1
                    else:
                        right -= 1
        return result
