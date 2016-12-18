class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #subsum[i:j] = sums[j-1] - sums[i-1] == k
        #sums[j-1] -k = sums[i-1] check if left ever equals to right
        #check input
        if not nums: return 0
        for i in xrange(1,len(nums)):
            nums[i] += nums[i-1]
        map = dict()
        map[0] = -1
        lsub = 0
        for i in xrange(len(nums)):
            if nums[i] - k in map:
                lsub = max(lsub, i - map[nums[i] - k])
            if nums[i] not in map:
                map[nums[i]] = i
        return lsub
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #check input
        # if not nums: return 0
        # l = len(nums)
        # for i in xrange(1,l):
        #     nums[i] += nums[i-1]
        # map = dict()
        # map[0] = -1
        # lsub = 0
        # for i in xrange(l):
        #     if nums[i]-k in map:
        #         lsub = max(lsub, i- map[nums[i]-k])
        #     if nums[i] not in map:
        #         map[nums[i]] = i
        # return lsub