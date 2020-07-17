#lc solution
#combine of #2 and #3, binary search on each row, update right bound when there are leftmost 1 appeared further left.
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        leftMost1Idx = n-1
        has1 = False
        for i in range(m):
            l, r = 0, leftMost1Idx
            while l <= r:
                mid = (l + r)//2
                if binaryMatrix.get(i, mid): # if 1
                    if mid >0 and not binaryMatrix.get(i, mid-1): #if 1 step left is 0
                        break
                    r = mid -1
                else: # if 0
                    l = mid + 1
            if binaryMatrix.get(i, mid): # if 1, then [i,mid] is the left most 1 in this row
                has1 = True
                leftMost1Idx = mid
        return leftMost1Idx if has1 else -1
