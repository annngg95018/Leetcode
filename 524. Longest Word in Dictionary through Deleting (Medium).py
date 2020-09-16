d.sort(key = lambda x : (-len(x), x)) //利用 sort 進行排序 -len(x) 表示先依照字串長度降冪排序 x 表示再以序號排序，因為題目表示如果長度一樣則選較小順序的，故以升冪排序
        for word in d:  //將 d 中的字串一個一個拉出來做比較
            a = 0
            b = 0
            
            while a < len(s) and b < len(word): //如果參數 a b 都小於 s 以及 word 的長度則繼續執行
                if s[a] == word[b]: //若當前s中的字母與word中的字母相同
                    a += 1 //則指針a b +1 繼續往下比
                    b += 1
                
                else:
                    a += 1 //若沒有的話 s 中的指針 a 繼續往下尋找有相同的字母
            
            if len(word) == b:  //如果當前word字串裡的字母，都在 s 字串中的話，那麼指針 b 的步數便會與 word 的長度相同，則返回其字串 word，因為已經以降冪排序所以返回的便為最長的字串
                return word
        
        return "" //一題目要求若沒有結果的話則返回空集合“”
        
        https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/sortshuang-zhi-zhen-by-bei-ming-you-yu-32/
        https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/524tong-guo-shan-chu-zi-mu-pi-pei-zi-dian-li-zui-c/
        https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/shuang-zhi-zhen-zi-fu-chuan-an-zi-dian-xu-pai-xu-b/
