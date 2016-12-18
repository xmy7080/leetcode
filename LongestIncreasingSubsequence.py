class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #check input
        l = len(nums)
        if l <=1: return l
        #fill each lenth of increase as base "1"
        li = [1] * l
        for i in xrange(l):
            for j in xrange(0,i):
                if nums[j] < nums[i]:# if curr num add one more increse length, try update li[i]
                    if li[j] + 1 > li[i]:
                        li[i] = li[j]+1
        return max(li)