#=======two pointers========
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
#=======stack approach========
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # stk = [ (height[0], 0) ]
        water = 0
        stk = []
        for cur in range(len(height)):
            while len(stk) > 1 and height[cur] > height[ stk[len(stk)-1] ]:
                top = stk.pop()
                boundDistance = cur - stk[len(stk)-1] - 1
                boundHeight = min(height[cur], height[ stk[len(stk)-1] ]) - height[top]
                if boundHeight < 0: break
                water += boundDistance * boundHeight
            stk.append(cur)
        
        return water
                
                    
