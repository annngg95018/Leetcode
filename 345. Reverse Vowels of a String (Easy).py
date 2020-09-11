class Solution:
    def reverseVowels(self, s: str) -> str:
        low, high = 0, len(s) - 1
        s = list(s)
        res = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        while low < high:
            while low < high and s[high] not in res:
                high -= 1
            while low < high and s[low] not in res:
                low += 1
            
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
            
        return "".join(s) // .join print出來為一個自串list的""為取代逗號的內容如果是
 -----------------------------------------------------
 
 class Solution:
    def reverseVowels(self, s: str) -> str:
        low, high = 0, len(s) -1
        s = list(s)
        vowel = set("aeiouAEIOU")// 用set
        
        while low < high:
            if s[low] in vowel and s[high] in vowel:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
                
            if s[low] not in vowel:// if --- not = if not ---
                low += 1
            if s[high] not in vowel:
                high -= 1
        
        return "".join(s)
 
