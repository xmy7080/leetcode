#a more pythonic way, and it takes any square number matrix===
#from chime onsite
class Solution(object):
    def checkValidPart(self, lt):
        #PR reviews: make lth as a global variable
        lth = len(lt)
        dic = collections.defaultdict(int)
        for n in lt:
            if n.isdigit():
                digit = int(n) 
            else: continue
            if digit in range(1, lth+1):
                dic[digit] += 1
            else:
                return False
        for i in dic:
            if dic[i] != 1:
                return False
        return True
    
    def isValidSudoku(self, matrix):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #lth will be always square numbers
        lth = len(matrix)
        boxL = int(math.sqrt(lth))
        #check rows and cols first
        for i in xrange(lth):
            if not self.checkValidPart(matrix[i]):
                return False
        
        for j in xrange(lth):
            cols = [row[j] for row in matrix]
            if not self.checkValidPart(cols):
                return False
        
        #check boxes
        for i in xrange(0,lth-boxL+1,boxL):
            rows = matrix[i: i+boxL]
            for j in xrange(0, lth-boxL+1, boxL):
                #box is what we need to check
                box = [row[j:j+boxL] for row in rows ]
                listBox = [y for row in box for y in row]
                if not self.checkValidPart(listBox):
                    return False
        return True
#=====
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check input
        if not len(board):
            return True
        m, n = len(board), len(board[0])
        
        #check rows
        for i in xrange(0,m):
            tmplist = []
            for j in xrange(0,n):
                tmplist.append(board[i][j])
            if not self.helper(tmplist):
                return False
        
        #check cols
        for j in xrange(0,n):
            tmplist = []
            for i in xrange(0,m):
                tmplist.append(board[i][j])
            if not self.helper(tmplist):
                return False
        
        #check 3X3 squares
        for i in xrange(0, m/3):
            for j in xrange(0, n/3):
                tmplist = []
                for a in xrange(i*3,i*3+3):
                    for b in xrange(j*3,j*3+3):
                        tmplist.append(board[a][b])
                if not self.helper(tmplist):
                    return False
        
        return True
        
    def helper(self,tmplist):
        s = set()
        for l in tmplist:
            if l == ".": continue
            else:
                if l in s:
                    return False
                s.add(l)
        return True
