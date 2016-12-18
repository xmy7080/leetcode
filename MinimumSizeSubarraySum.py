class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #check input
        if not nums: return 0
        i, j = 0, 1
        #subarray is nums[i:j], [0,1,2,3][1:2] = [1]
        sum = nums[0]
        lsub = len(nums)
        found = False
        while i<j and j<len(nums):
            #move the j downward when sum < s
            while sum < s and j<len(nums):
                sum += nums[j]
                j += 1
            #move the i downward when sum >= s
            while sum >= s and i<j:
                found = True
                lsub = j-i if lsub>j-i else lsub
                sum -= nums[i]
                i += 1
        if found:
            return lsub
        else:
            return 0