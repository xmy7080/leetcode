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
            
=======old school way to sort and use l r pointers, pay attention to zip the index first======
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        zips = zip(nums, range(len(nums)))
        zips.sort()
        l, r = 0, len(zips) - 1
        while l < r:
            sm = zips[l][0] + zips[r][0]
            if sm < target:
                l += 1
            elif sm > target:
                r -= 1
            else:
                return [zips[l][1], zips[r][1] ]
