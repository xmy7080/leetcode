#delta indicats the first pair that are not equal, then we check all the delta after wards, as long as we find it comes with different sign, 
#return false
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        delta = 0
        for i in range(len(A)-1):
            tmpd = A[i+1] - A[i]
            if not delta and tmpd:
                delta = tmpd
                continue
            if delta and tmpd and delta* tmpd <0:
                return False
        return True
