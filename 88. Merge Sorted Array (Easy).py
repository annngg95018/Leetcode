pointer1 = m-1
        pointer2 = n-1
        pointer3 = m+n-1

        while pointer1 >=0 and pointer2 >=0:
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
                pointer3 -= 1
            elif nums1[pointer1] < nums2[pointer2]:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
                pointer3 -= 1

        if pointer1 < 0:
            nums1[0:pointer2 + 1] = nums2[0:pointer2 + 1]
           
  --------------------------------------------------------------
  
   pointer2 = n -1
        pointer3 = m + n -1
        
        while pointer1 >= 0 and pointer2 >= 0: //注意要有等號
            if nums1[pointer1] >= nums2[pointer2]: // 注意要有等號不然程式會crash
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
                pointer3 -= 1
            
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
                pointer3 -= 1
        nums1[:pointer2 + 1] = nums2[:pointer2 + 1] 
        
        //reference:https://leetcode-cn.com/problems/merge-sorted-array/solution/shuang-zhi-zhen-cong-hou-xiang-qian-cha-zhu-xing-j/
                    https://leetcode-cn.com/problems/merge-sorted-array/solution/guan-fang-jie-fa-3fan-xiang-shuang-zhi-zhen-de-xia/
