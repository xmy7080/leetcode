class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,len(height)-1#two pointers
        hl, hr = 0, 0 #highest left and highest right so far
        vol = 0
        while l<=r:
            if height[l] <= height[r]:
                if hl < height[l]: hl = height[l]#current left wall exceed old hight, updated hl
                else:#hl over current height, calculate rain amount
                    vol += hl - height[l]
                l+=1
            else:
                if hr < height[r]: hr = height[r]
                else:
                    vol += hr - height[r]
                r -=1
        return vol
                    