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

#some follow up for decimal numbers in string(fb interviews)
def addStrings(a: str, b: str) -> str:
    def countsDecimal(m: str) -> int:
        occur = m.find('.')
        return len(m) - occur -1 if occur != -1 else 0
    #reused this func
    def intsHelper(a: str, b: str) -> str:
        la, lb = len(a)-1, len(b)-1
        carry, tot = 0, 0
        res = []
        while la >= 0 or lb >= 0:
            tmpa = int(a[la]) if la >= 0 else 0
            tmpb = int(b[lb]) if lb >= 0 else 0
            tot = tmpa + tmpb + carry
            carry = tot // 10
            res[0:0] = str(tot % 10)
            la -= 1
            lb -= 1
        if carry:
            res[0:0] = str(carry)
        return "".join(res)
    #count decimals in a and b, padding to one that are shorter in decimal
    #then remove decimal, treat both as integers, reuse the addStrings original function
    dciA, dciB = countsDecimal(a), countsDecimal(b)
    #remove '.' from a and b, if any has
    a = a.replace('.', '')
    b = b.replace('.', '')
    pad0s = abs(dciA - dciB)
    if dciA > dciB:
        b = b+'0'* pad0s
    elif dciA < dciB:
        a = a+'0'* pad0s
    
    midRes = intsHelper(a, b)
    dotIdx = max(dciA, dciB)
    #remember to put dot back to the right position
    return midRes[:-dotIdx] + '.' + midRes[-dotIdx:] if dotIdx else midRes
    

a = "1278.401"
b = "49.899"
print(addStrings(a, b))
