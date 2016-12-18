class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        notzero, nottwo = 0, l-1 
        #notzero save the place first not zero digit, 
        #nottwo for first digit not 2 counting from end
        #check input
        if l <= 1: return
        i = 0
        while i<=nottwo and i < l:
            if nums[i] == 0:
                nums[i] = nums[notzero]
                nums[notzero] = 0
                notzero += 1
                i+= 1
            elif nums[i] == 2:
                nums[i] = nums[nottwo]
                nums[nottwo] = 2
                nottwo -= 1
            else:
                i += 1
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # zero, second = 0, len(nums)-1
        # i = 0
        # while i<=second:
        #     if nums[i] == 0:
        #         nums[i] = nums[zero]
        #         nums[zero] = 0
        #         zero += 1
        #     if nums[i] == 2:
        #         nums[i] = nums[second]
        #         nums[second] = 2
        #         second -= 1
        #         i -= 1
        #     i += 1
        # return