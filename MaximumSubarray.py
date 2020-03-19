#====convention way of using dp, O(n) time and O(n) space====
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [nums[0]] + [0] * (len(nums)-1)
        for i in xrange(1, len(nums)):
            ans[i] = max(nums[i], ans[i-1] + nums[i])
        return max(ans)

#====here is O(n) time and O(1) space approach, collapse the dp array into one variable===
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
