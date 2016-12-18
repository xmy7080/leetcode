class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        sumhere = nums[0]
        res = nums[0]
        for n in nums[1:]:
            sumhere = max(sumhere + n, n)
            res = max(res,sumhere)
        return res