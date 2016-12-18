class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lth = len(nums)
        if lth == 0: return 0
        s, e = 0, lth-1
        while s <e:
            m = s + (e-s)/2
            if nums[m] < nums[e]:#[6,1,2,3,4]
                e = m
            elif nums[m] > nums[e]:#[5,6,2,3]
                s = m+1
            else:
                e -=1
        return nums[s]
        