class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        i = 0
        nextunq = 1
        while nextunq < n:
            if nums[i] != nums[nextunq]:
                i += 1
                nums[i] = nums[nextunq]
            else:
                nextunq += 1
        return i+1
            
    