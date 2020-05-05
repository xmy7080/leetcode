#basic two pointer solution
#need sort upfront, also the findOverlap function is simplified than the part commented out
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        def findOverlap(earlier, later): #[1,5][4,6]   [1,8][4,6]
            start, end = max(earlier[0], later[0]), min(earlier[1], later[1])
            return [start, end] if start < end else []
            # if earlier[1] <= later[0]:#[1,5][7,9]
            #     return []
            # else:#[1,5][4,6] => [4,5]
            #     return [later[0], earlier[1]]
        slots1.sort()
        slots2.sort()
        i, j, m, n = 0, 0, len(slots1), len(slots2)
        while i<m and j < n:
            if slots1[i][0] < slots2[j][0]:
                overlap = findOverlap(slots1[i], slots2[j])
            else:
                overlap = findOverlap(slots2[j], slots1[i])
            if overlap and overlap[1] - overlap[0] >= duration:
                return [overlap[0], overlap[0]+duration]
            if slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1
        return []
                
                    
        
