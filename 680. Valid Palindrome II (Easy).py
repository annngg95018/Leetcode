class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) -1
        while i <= j :
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                x = s[i:j] //範圍是i~j-1
                y = s[i+1:j+1]
                return True if x[::-1] == x or y[::-1] == y  else False //[::-1] 倒敘
            
        return True
