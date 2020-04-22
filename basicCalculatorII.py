#solution from https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.
#mind the case when int(-3/2) => -2, hence we add the float() conversion
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack, operand, prevSign = [], 0, '+'
        for i in xrange(len(s)):
            if s[i].isdigit():
                operand = operand * 10 + int(s[i])
            # print("operand is " + str(operand))
            if s[i] in "+-*/" or i == len(s)-1:
                if   prevSign == '+':
                    stack.append(operand)
                elif prevSign == '-':
                    stack.append(-operand)
                elif prevSign == '*':
                    stack.append(stack.pop() * operand )
                elif prevSign == '/':
                    stack.append(int(stack.pop() / float(operand)) )
                prevSign, operand = s[i], 0
            # print("stack is " + str(stack) + " " + str(operand))
        return sum(stack)
