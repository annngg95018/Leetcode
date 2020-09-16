class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head.next //也可以是fast = head
        
        while fast and fast.next: // 如果 fast 還有 fast.next都存在 防止空集合及下個指標為空，while裡的條件為True才會執行，此題中若快指標還有下個快指標都存在則執行迴圈底下的條件式
            if fast == slow:  // 當快與慢指標相遇 表示有環
                return True
            slow = slow.next
            fast = fast.next.next //因為條件為fast.next 
            
        return False // 跳出迴圈表示快慢指標不存在所以回傳False

      ---------------------------------------------------------
      class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        slow = head
        fast = head
        
        while slow != fast
            if fast is None and fast.next is None: //如果有快慢兩個指標 利用快的那個做判斷
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True //跳出迴圈表示快慢指標相等 所以回傳 True
      
  兩題關鍵差在 while 的條件 第一個為 fast 與 slow 快慢指標都存在 裡面執行等到兩個相等，第二個為在兩個不相等的前提下若塊指標的當下以及下個指向為None則回傳False 若跳出迴圈變表示快慢指標相等，回傳True
  
Referece:
  https://leetcode-cn.com/problems/linked-list-cycle/solution/pythonkuai-man-zhi-zhen-by-mu-qian-ruo-chi/
  https://leetcode-cn.com/problems/linked-list-cycle/solution/141-linked-list-cycle_li-jie-by-gulugulu_go/
  https://leetcode-cn.com/problems/linked-list-cycle/solution/python3-shuang-zhi-zhen-141-by-littlelion_njuer/
  https://leetcode-cn.com/problems/linked-list-cycle/solution/zhe-shi-yi-ge-you-qu-de-shi-pin-ti-jie-kuai-man-zh/
  https://leetcode-cn.com/problems/linked-list-cycle/solution/python-pu-tong-lie-biao-de-in-he-shuang-zhi-zhen-k/
  
