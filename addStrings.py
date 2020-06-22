#exactly same with add binary, just put scale from 2 to 10
class Solution:
    def addStrings(self, a: str, b: str) -> str:
        la, lb = len(a)-1, len(b)-1
        res = []
        carry, sum = 0, 0
        while la >= 0 or lb >= 0:
            numa = int(a[la]) if la >=0 else 0
            numb = int(b[lb]) if lb >=0 else 0
            sum = numa + numb + carry
            res[0:0] = str(sum%10)
            carry = sum//10
            la -= 1
            lb -= 1
        if carry:
            res[0:0] = str(carry)
        return ''.join(res)
