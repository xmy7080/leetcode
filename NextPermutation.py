#a bit easier solution of reusing swap logic. also we put logic: finding the first number on the right bigger than 4
#out of the helper function
#check here https://leetcode.com/articles/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, a, b) -> None:
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp
        
        def reverse(nums, a) -> None:
            l, r = a, len(nums)-1
            while l < r:
                swap(nums, l, r)
                l += 1
                r -= 1
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums)-1
            while j>i and nums[j] <= nums[i]:
                j -= 1
            swap(nums, i, j)
        reverse(nums, i+1)
        
#=============
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
