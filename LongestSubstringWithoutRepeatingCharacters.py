class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l, r = 0, 0
        check = set()
        isover = False
        while r<len(s):
            if s[r] not in check:#when input will not broken condition, add it in
                check.add(s[r])
                r += 1
            else:#when meet dup
                isover = True
            while isover and s[l] != s[r]:
                check.remove(s[l])
                l += 1
            res = max(res, r-l)
            if r<len(s) and s[l] == s[r]:
                isover = False
                l+= 1
                r += 1
        # res = max(res, r-l)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not s: return 0
        # save = set()
        # l, r, maxl = 0,0,0
        # #say s is "acbcd"
        # while r<len(s):
        #     if s[r] not in save:#"" to acbc
        #         save.add(s[r])
        #         r+=1
        #         continue#continue(not while) because we need make sure r<len(s)
        #     maxl = max(maxl, r-l)
        #     while s[l] != s[r]:#acbc to cbc
        #         save.remove(s[l])
        #         l+=1
        #     #cbc to bcd
        #     l+=1
        #     r+=1
        # maxl = max(maxl, r-l)
        # return maxl
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if(s==null||s.length()==0) return 0;
        # Set<Character> set = new HashSet<Character>();
        # int l = 0, r = 0;
        # int maxLen = 0;
        # while(r<s.length()){
        #     if(!set.contains(s.charAt(r))){
        #         set.add(s.charAt(r++));
        #         continue;
        #     }
        #     maxLen = Math.max(maxLen, r-l);
        #     while(s.charAt(l)!=s.charAt(r)){
        #         set.remove(s.charAt(l++));
        #     }
        #     l++;
        #     r++;
        # }
        # maxLen = Math.max(maxLen, r-l);
        # return maxLen;