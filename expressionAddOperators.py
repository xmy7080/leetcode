#lc solution
#https://leetcode.com/articles/expression-add-operators/
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        lth = len(num)
        ans = []
        def recurse(idx, prevOperand, currOperand, value, expression) -> None:
            if idx == lth:
                if value == target and currOperand == 0:
                    #[1:] for remove the leading '+'
                    ans.append("".join(expression[1:]))
                #exit recurse anyway as long as idx is out of bound
                return
            
            currOperand = currOperand * 10 + int(num[idx])
            strOp = str(currOperand)
            
            #concatenate case 2*10 + 3 -> 23, also 05 is not a valid number, hence the check
            if currOperand != 0:
                recurse(idx+ 1, prevOperand, currOperand, value, expression)
            
            #addition
            expression.append('+');expression.append(strOp)
            recurse(idx+1, currOperand, 0, value + currOperand, expression)
            expression.pop(); expression.pop()
            
            # Can subtract or multiply only if there are some previous operands
            if expression:
                #substraction
                expression.append('-');expression.append(strOp)
                recurse(idx+1, -currOperand, 0, value - currOperand, expression)
                expression.pop(); expression.pop()

                #multiply
                #prevOperand only useful here, cause we need reverse the last possible wrong + or - (by substract prevOperand), then multiply for the currOperand
                expression.append('*');expression.append(strOp)
                recurse(idx+1, currOperand*prevOperand, 0, value - prevOperand + (currOperand*prevOperand), expression)
                expression.pop(); expression.pop()
        
        recurse(0, 0, 0, 0, [])
        return ans
