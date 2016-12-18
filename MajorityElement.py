class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = nums[0]
        count = 1
        for n in nums[1:]:
            if count == 0:
                count = 1
                maj = n
            elif maj == n:
                count += 1
            else:
                count -=1
        return maj