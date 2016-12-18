class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        if not tokens: return 0
        for c in tokens:
            if c in ['+','-','*','/']:
                operb = int(stk.pop())
                opera = int(stk.pop())
                if c == '+':
                    stk.append(opera + operb)
                elif c == '-':
                    stk.append(opera - operb)
                elif c == '*':
                    stk.append(opera * operb)
                elif c == '/':
                    stk.append(int( float(opera) / operb ) )
            else:
                stk.append(c)
        return int(stk.pop())