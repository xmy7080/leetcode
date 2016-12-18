class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums,[],res)
        return res
        
    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
        i = 0
        while i < len(nums):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]],res)
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        