#two pointer, from left to right
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(A)-1
        ans = []
        while l <= r:
            if A[l] ** 2 > A[r] ** 2:
                ans.append(A[l] ** 2)
                l += 1
            else:
                ans.append(A[r] ** 2)
                r -= 1
        return ans[::-1]
