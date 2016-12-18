class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums,[],res)
        return res
        
    def dfs(self,nums,path,res):
        if len(nums) == 0:
            res.append(list(path))
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     res = []
    #     self.dfs(nums,[],res)
    #     return res
        
    # def dfs(self,nums,path,res):
    #     if not nums:
    #         res.append(path)
    #     for i in xrange(len(nums)):
    #         self.dfs(nums[:i] + nums[i+1:],path+[nums[i]],res)
            