class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            if d.get(n,0): return True
            d[n] = 1
        return False