class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for c in s:
            if c in ['[','{','(']:
                stk.append(c)
            if stk:
                if c == ']' and stk.pop() != '[':
                    return False
                elif c == '}' and stk.pop() != '{':
                    return False
                elif c == ')' and stk.pop() != '(':
                    return False
            else:
                return False
        return not stk
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stk = []
        # for c in s:
        #     if c in ['(','[','{']:
        #         stk.append(c)
        #     elif stk:
        #         if c == ')' and stk.pop() !=  '(':
        #             return False
        #         elif c == ']' and stk.pop() !=  '[':
        #             return False
        #         elif c == '}' and stk.pop() !=  '{':
        #             return False
        #     elif not stk:
        #         return False
        # return not stk