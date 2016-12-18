class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = len(nums)-1
        while i>=1:#find 4 in 947651
            if nums[i] > nums[i-1]:
                break
            i -= 1
        if i != 0:
            self.swap(nums,i-1)#swap 5 and 4 in 947651
        
        self.reverse(nums,i)#reverse rest in 957641 to 951467
    
    def swap(self,nums,i):
        for n in xrange(len(nums)-1,i,-1):
            if nums[n] > nums[i]:
                tmp = nums[i]
                nums[i] = nums[n]
                nums[n] = tmp
                return
    
    def reverse(self,nums,i):
        start, end = i, len(nums)-1
        while start < end:
            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp
            start += 1
            end -= 1