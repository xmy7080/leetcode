class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        up = 1
        ans = 1
        for i in xrange(len(nums)):
            if i == 0:
                continue
            up    = (up   + 1) if nums[i] > nums[i-1] else 1
            ans = max(ans, up)
        return ans
