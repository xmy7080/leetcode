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