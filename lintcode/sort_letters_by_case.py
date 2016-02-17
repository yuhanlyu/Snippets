class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left].islower():
                left += 1
            while left < right and chars[right].isupper():
                right -= 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
