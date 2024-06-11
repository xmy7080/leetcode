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
                res = i # this is not guarantee to be hit, therefore -1 may be returned for a actual existing value
        return res
        
# 
# a better solution should be
def __init__(self, nums: List[int]):
    self.nums = nums

def pick(self, target: int) -> int:
    cnt = idx = 0
    for i, num in enumerate(self.nums):
        if num != target:
            continue
        if cnt == 0:
            idx = i
            cnt = 1
        else:
            # this random will already give me numbers
            # between 0 and cnt inclusive
            # so for 2nd number I am getting random number 0 and 1
            # so each having a probability of 1/2
            # similarly for three numbers it will be 1/3
            rnd = random.randint(0, cnt)
            if (rnd == cnt):
                idx = i
            cnt += 1
    
    return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
