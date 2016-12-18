class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = []
        closest = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]: continue
            goal = target-nums[i]
            j = i + 1
            k = len(nums)-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if abs(target-sum)<abs(target-closest):
                    closest = sum
                if closest == target: return target
                if sum>target: k-=1
                if sum<target: j+=1
                while j<k and nums[j]==nums[j-1]: j+=1
                while j<k and k<len(nums)-1 and nums[k]==nums[k+1]: k-=1
        return closest