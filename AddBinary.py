class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a)-1, len(b)-1
        res = []
        carry, sum = 0, 0
        while la >= 0 or lb >= 0:
            numa = int(a[la]) if la >=0 else 0
            numb = int(b[lb]) if lb >=0 else 0
            sum = numa + numb + carry
            res[0:0] = str(sum%2)
            carry = sum/2
            la -= 1
            lb -= 1
        if carry:
            res[0:0] = '1'
        return ''.join(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # la = len(a)-1
        # lb = len(b)-1
        # carry = 0
        # res = []
        # while la >= 0 or lb >= 0:
        #     inta = int(a[la]) if la >= 0 else 0
        #     intb = int(b[lb]) if lb >= 0 else 0
            
        #     sum = inta + intb + carry
        #     res[0:0] = str(sum%2)
        #     carry = sum/2
        #     la -= 1
        #     lb -= 1
        # if carry: res[0:0] = str(carry)
        # return ''.join(res)