class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n: return True
        for i, x in enumerate(flowerbed):
            if not x and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
            if not n: #once all plant was put down
                return True
        return False
                    
        
        #solution below is wrong, only gets all possible spot a plant can be at. but didn't consider once some plant was down, the adjacent spot are unavailable
        # l, r = flowerbed[1:] + [0], [0] + flowerbed[:-1] #shift one left and one right
        # allPossibleBed = map(lambda x,y,z: x|y|z, flowerbed, l, r)
        # return n <= allPossibleBed.count(0)
