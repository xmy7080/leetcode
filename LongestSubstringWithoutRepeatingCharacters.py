#simpler sliding window implement from leetcode solution
#https://leetcode.com/articles/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lth = len(s)
        l, r = 0, 0
        save = set()
        ans = 0
        while l < lth and r < lth:
            if s[r] not in save:
                save.add(s[r])
                r += 1
                ans = max(ans, r -l)
            else:
                save.remove(s[l])
                l += 1
        return ans
#sliding window optimized way, using hashmap to store when did curr char last appear, leetcode solution====
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lth = len(s)
        hmap = {}
        ans = 0
        i = 0
        for j in xrange(0, lth):
            if s[j] in hmap:
                i = max(i, hmap[s[j]] + 1)
            ans = max(ans, j -i + 1)
            hmap[s[j]] = j
        return ans
=================
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
================
        
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
