#===jiuzhang dp exmaple approach, using 1 dimensional array, fast but O(n) space====
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxl = [0] * len(nums)
        minl = [0] * len(nums)
        maxl[0], minl[0] = nums[0], nums[0]
        for i, n in enumerate(nums):
            if i == 0:
                continue
            maxl[i] = max(n, max(n * maxl[i-1], n * minl[i-1]) )
            minl[i] = min(n, min(n * maxl[i-1], n * minl[i-1]) )
        return max(maxl)
    
#===optimized for rolling array (1 demensional array collapse to a single number)====
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minh = nums[0]
        maxh = nums[0]
        maxp = nums[0]
        
        for n in nums[1:]:
            a = maxh * n
            b = minh * n
            maxh = max( max(a,b), n)
            minh = min( min(a,b), n)
            maxp = max(maxp,maxh)
        return maxp
