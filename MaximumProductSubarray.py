class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minh = nums[0]
        maxh = nums[0]
        maxp = nums[0]
        
        for n in nums[1:]:
            a = maxh * n
            b = minh * n
            maxh = max( max(a,b), n)
            minh = min( min(a,b), n)
            maxp = max(maxp,maxh)
        return maxp