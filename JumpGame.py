#===dp bottom top approach, very slow but passed===
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = [False] * len(nums)
        ans[0] = True
        for i, n in enumerate(nums):
            if ans[i]:
                minSpan = min(i+n, len(nums)-1)
                ans[i:minSpan+1] = [True] * (minSpan -i + 1)
        return ans[len(nums)-1]
#===dp bottom top appraoch, jiuzhang example approach, but will exceed in time===
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = [False] * len(nums)
        ans[0] = True
        for i in xrange(1, len(nums)):
            for x in xrange(i):
                if ans[x] and x + nums[x] >= i:
                    ans[i] = True
                    break
        return ans[len(nums)-1]
#===below is the greedy approach O(n) time and O(1) space
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        m = 0
        for i in xrange(l):
            if i > m: return False
            m = max(nums[i] + i,m)
        return True
