class Solution:
    def judgeSquareSum(self, c: int) -> bool:
      i, j = 0, int(math.sqrt(c))
      
      while i < j:
        powerSum = i ** 2 + j ** 2
        if powerSum == c:
          return True
          
        efif c < powerSum:
          j -= 1
          
        else:
          i += 1
          
      return False
          
      
