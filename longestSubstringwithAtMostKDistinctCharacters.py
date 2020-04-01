#====same way derived from leetcode longest non repeat char====
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not len(s) or not k: return 0
        l, r = 0, 0
        hmap = {}
        ans = 0
        while r < len(s):
            if len(hmap) < k or s[r] in hmap:
                hmap[s[r]] = hmap.get(s[r], 0) + 1
                r += 1
                ans = max(ans, r -l)
            else:
                if hmap[s[l]] == 1:
                    del hmap[s[l]]
                elif hmap[s[l]]:
                    hmap[s[l]] -= 1
                l += 1
        return ans
