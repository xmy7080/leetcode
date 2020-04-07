class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        def isOverlap(A, B):
            return not (A[1] < B[0] or A[0] > B[1])
        def mostCommon(A, B):
            return [max(A[0],B[0]), min(A[1], B[1])]
        
        if not A or not B: return []
        la, lb = len(A), len(B)
        a, b = 0, 0
        ans = []
        while a < la and b < lb:
            if isOverlap(A[a], B[b]):
                ans.append(mostCommon(A[a], B[b]) )
            if A[a][1] > B[b][1]:
                b += 1
            else:
                a += 1
        return ans
