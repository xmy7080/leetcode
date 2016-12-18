class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0] * (m+ n)
        
        for i in xrange(m-1,-1,-1):
            for j in xrange(n-1,-1,-1):
                mul = int(num1[i])* int(num2[j])
                p1, p2 = i+j, i+j+1
                sum = mul + res[p2]
                
                res[p1] += sum/10
                res[p2] = sum%10
        
        r = ''
        for n in res:
            if not (r == '' and n==0):
                r += str(n)
        return r if r else '0'