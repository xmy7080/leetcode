#hashset way of doing 2 sum on each go of pivet number
#also dedupe the result by saving 3-elements tuples in result set
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        for i in xrange(len(nums)):
            target = -1 * nums[i]
            s = set()
            for j in xrange(i+1, len(nums)):
                if target - nums[j] in s:
                    tmp = [nums[i], target - nums[j], nums[j]]
                    tmp.sort()
                    ans.add((tmp[0], tmp[1], tmp[2]))
                else:
                    s.add(nums[j])
        return [ triplet for triplet in ans]
    
#sort the list and do two pointers approach on each go of pivet number
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            target = 0 - nums[i]
            while j<k:
                if (nums[j] + nums[k]) > target:
                    k-=1
                elif (nums[j] + nums[k]) < target:
                    j+=1
                else:
                    tmp = [nums[i],nums[j],nums[k]]
                    res.append(tmp)
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return res
