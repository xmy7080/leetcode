#the description is awlfully written, check explain here
#https://leetcode.com/problems/next-greater-element-i/discuss/97614/Confusing-statement
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        i = n-1
        ans = [-1] * m
        stk = []
        mp = {}
        for i in range(n-1, -1, -1):
            while stk and stk[len(stk)-1] < nums2[i]:
                stk.pop()
            mp[nums2[i]] = stk[len(stk)-1] if stk else -1
            stk.append(nums2[i])
        for i in range(m):
            ans[i] = mp[nums1[i]]
        return ans
