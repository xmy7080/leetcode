class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums: return [[]]
        res = [[]]
        tmp = []
        self.helper(nums,0,res,tmp)
        return res
    
    def helper(self,nums,start,res,tmp):
        for i in xrange(start,len(nums)):
            tmp.append(nums[i])
            res.append(list(tmp))
            self.helper(nums,i + 1, res,tmp)
            tmp.pop()
        return