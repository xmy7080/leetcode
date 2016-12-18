class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.firstGreaterEqual(nums,target)
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        return [first, self.firstGreaterEqual(nums,target+1)-1]
        
    def firstGreaterEqual(self, nums, target):
        s, e = 0, len(nums)
        while s<e:
            mid = (s+e)/2
            if nums[mid]<target:
                s = mid + 1
            else:
                e = mid
        
        return s
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # first = self.firstGreaterEqual(nums,target)
        # if first == len(nums) or nums[first] != target:
        #     return [-1,-1]
        # return [first, self.firstGreaterEqual(nums,target+1)-1]
        
    # def firstGreaterEqual(self,nums,target):
    #     s, e = 0, len(nums)
    #     while s<e:
    #         mid = s + (e-s)/2
    #         if nums[mid] < target:
    #             s = mid + 1
    #         else:
    #             e = mid
    #     return s
        
         
        
    # def firstGreaterEqual(self, nums, target):
    #     low, high = 0, len(nums)
    #     while low < high:
    #         mid = low + ((high - low)>>1)
    #         if nums[mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low