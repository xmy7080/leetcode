class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(res, "", n,n)
        return res
        
    def helper(self, res, sb, left, right):
        if left == right == 0:
            res.append(sb)
        if left >0 and left<=right:
            sb += '('
            self.helper(res,sb, left-1,right)
            sb = sb[:-1]
        if right >0 and left < right:
            sb += ')'
            self.helper(res,sb,left,right-1)
            sb = sb[:-1]