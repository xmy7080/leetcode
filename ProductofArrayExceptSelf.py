#=====most neat and concise approach, O(n) time and also in place space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # totalProduct = 1
        # for a in A:
        #     totalProduct *= a
        #totalProduct == 0 if [2,3,4,0, 5,6]
        # 2*3*4   5*6
        if not nums: return []
        lth = len(nums)
        ans = [1] * lth
        p = 1
        for i in xrange(1,lth):
            p *= nums[i-1]
            ans[i] *= p
        p = 1
        for i in xrange(lth-2, -1, -1):
            p *= nums[i+1]
            ans[i] *= p
        return ans
#=====
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #inplace solution
        res = [1]*len(nums)
        mul = 1
        for i in xrange(len(nums)-1):
            mul *= nums[i]
            res[i] = mul
        mul = 1
        for i in xrange(len(nums)-1,-1,-1):
            if i == 0:
                res[i] = mul
            else:
                res[i] = res[i-1]*mul
            mul *= nums[i]
        return res
        
        
        # not in place solution
        # prodbef, prodaft = [1]*len(nums), [1]*len(nums)
        # mul, mulrev = 1, 1
        # for i in xrange(len(nums)-1):
        #     mul *= nums[i]
        #     prodbef[i] = mul
        # for i in xrange(len(nums)-1,0,-1):
        #     mulrev *= nums[i]
        #     prodaft[i] = mulrev
        # res = [1]*len(nums)
        # for i in xrange(len(nums)):
        #     bef = prodbef[i-1] if i-1>=0 else 1
        #     aft = prodaft[i+1] if i+1<len(nums) else 1
        #     res[i] = bef * aft
        # return res
