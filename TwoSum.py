class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1 // 第二數的命名
        
        while low < high:
            total =  numbers[low] + numbers[high] //total 必須擺在這裡
            if total == target:
                return(low + 1, high + 1)
            elif total < target:
                low += 1
            else:
                high -= 1
        return (-1, -1) //return -1 -1 表示錯誤
