#leetcode discussion solution and its first explain in comment
#randrange(1) will always return 0, (2) will evenly return [0,1], and so on.
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        count = 0
        for i in xrange(len(self.nums)):
            if self.nums[i] != target: 
                continue
            count += 1
            if random.randrange(count) == 0:
                res = i
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
