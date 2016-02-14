from collections import Counter
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        cA = Counter(list(A))
        cA.subtract(Counter(list(B)))
        for (x, c) in cA.items():
            if c < 0:
                return False
        return True
