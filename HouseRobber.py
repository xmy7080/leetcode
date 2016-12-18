class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevNo, prevYes = 0, 0
        for n in nums:
            tmpPrevNo = prevNo
            prevNo = max(prevNo,prevYes)
            prevYes = n + tmpPrevNo
        return max(prevYes,prevNo)