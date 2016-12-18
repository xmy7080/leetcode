class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #check input
        if not nums: return [[]]
        res = []
        tmp = []
        nums = sorted(nums)
        self.dfs(nums, tmp, 0, res)
        return res
    def dfs(self,nums, tmp, start, res):
        new = list(tmp)
        res.append(new)
        i = start
        while i<len(nums):
            tmp.append(nums[i])
            self.dfs(nums, tmp, i + 1, res)
            tmp.pop()
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            i += 1
        return