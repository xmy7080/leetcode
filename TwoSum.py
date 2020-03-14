class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        dic = {}
        for i in xrange(len(nums)):
            if nums[i] in dic and 2 * nums[i] == target:
                    return [dic[nums[i]],i]
            if nums[i] not in dic and target-nums[i] in dic:
                return [dic[target-nums[i]],i]
            dic[nums[i]] = i
            
            
            
=====better way with enumerate===
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, n in enumerate(nums):
            if target - n in dic:
                return [dic[target-n], i]
            else:
                dic[n] = i
            
