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

-------------------------------------------

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
      i, j = 0, int(math.sqrt(c))
      
       while i < j:
        if i*i + j*j = c:
            return True
        elif i*i + j*j > c:
            j -= 1
        else:
            i += 1
        
        return False
   
-------------------------------------------

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
      
        while i < j:
            if c == i*i + j*j :
                return True
            elif i*i + j*j > c:
                j -= 1
            else:
                i += 1
        
        return False
                    
          
          
      
