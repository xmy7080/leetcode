class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        m = 0
        for i in xrange(l):
            if i > m: return False
            m = max(nums[i] + i,m)
        return True