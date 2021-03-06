#===solution https://leetcode.com/articles/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxvol = 0
        while left < right:
            maxvol = max(maxvol,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxvol
