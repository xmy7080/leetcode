class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for i in xrange(len(nums)):
            if i > k:
                s.remove(nums[i-k-1])
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
        return False
        