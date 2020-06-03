#another self written solution, with sub routine and start, end point
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        up, left = 0, 0
        down, right = len(matrix)-1, len(matrix[0])-1
        ans = []
        def routine(i, up, left, down, right):
            l = [(0,1), (1,0), (0,-1), (-1,0)]
            starts = [(up, left), (up, right), (down, right), (down, left)]
            ends   = [(up, right), (down, right), (down, left), (up, left)]
            d = l[i]
            start, end = starts[i], ends[i]
            # print("start is " + str(start) )
            # print("end is " + str(end) )
            while True:
                ans.append(matrix[start[0]][start[1]])
                if start == end: break
                start = tuple(map(add, start,d))
            
        while True:
            for i in range(4):
                routine(i, up, left, down, right)
                
                if   i == 0: up    += 1
                elif i == 1: right -= 1
                elif i == 2: down  -= 1
                elif i == 3: left  += 1
                if up > down or left > right:
                    return ans
                
#===============original solution======
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if  not len(matrix):
            return res
        rowstart, rowend = 0, len(matrix)-1
        colstart, colend = 0, len(matrix[0])-1
        
        while rowstart <= rowend and colstart <= colend:
            for j in xrange(colstart,colend+1,1):#left_up to right_up
                res.append(matrix[rowstart][j])
            rowstart += 1
            
            for i in xrange(rowstart, rowend+1,1):#right_up to right_down
                res.append(matrix[i][colend])
            colend -= 1
            
            if rowstart <= rowend:#exclude the [[2,3]] return [2,3,2]case
                for j in xrange(colend,colstart-1,-1):#right_down to left_down
                    res.append(matrix[rowend][j])
            rowend -= 1
            
            if colstart <= colend:
                for i in xrange(rowend,rowstart-1,-1):#left_down to left_up
                    res.append(matrix[i][colstart])
            colstart += 1
        
        return res
