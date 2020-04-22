#starting from 0 and plus
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n: return [""]
        ans = []
        def helper(tmp, left, right):
            if len(tmp) == 2 * n:
                ans.append(tmp)
            if left < n:
                helper(tmp + '(', left + 1, right)
            if right < left:
                helper(tmp + ')', left, right + 1)
        helper("", 0, 0)
        return ans
# starting from n and minus
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
