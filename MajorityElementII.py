class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        can1,can2,ct1,ct2 = 0,1,0,0
        for n in nums:
            if n == can1: ct1+=1
            elif n == can2: ct2+=1
            elif ct1 == 0: can1,ct1 = n,1
            elif ct2 == 0: can2,ct2 = n,1
            else: ct1,ct2 = ct1-1,ct2-1
        return [i for i in [can1,can2] if nums.count(i)>len(nums)//3]