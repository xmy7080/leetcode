#lc solution
#https://leetcode.com/articles/continuous-subarray-sum/
#save the mapping from total mod k to the index of the total mode k's first appearence
#check the index distance, if larger than 1 then call True
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {0:-1}
        tot = 0
        for i, n in enumerate(nums):
            tot += n
            if k:
                tot = tot % k
            if tot in m:
                if i - m[tot] >1:
                    return True
            else:
                m[tot] = i
        return False
