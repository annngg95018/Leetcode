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
        
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
                pointer3 -= 1
            
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
                pointer3 -= 1
        nums1[:pointer2 + 1] = nums2[:pointer2 + 1] 