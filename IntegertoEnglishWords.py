#selfmade solution, using string concatenante at the end
class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        ths = [None, 'Thousand', 'Million', 'Billion']
        oneToTeens = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        def getThousand(num) -> [str]:
            tmp = []
            lessHundred = num % 100
            if lessHundred < 20:
                tmp = [oneToTeens[lessHundred-1]] + tmp if lessHundred else tmp
            else:
                tenCounts = lessHundred // 10
                oneCounts = lessHundred % 10
                tmp = [oneToTeens[oneCounts-1]] + tmp if oneCounts else tmp
                tmp = [tens[tenCounts-2]] + tmp
            handredCounts = num // 100
            tmp = [oneToTeens[handredCounts-1], 'Hundred'] + tmp if handredCounts else tmp
            return tmp
                
        ans = []
        thCounts = 0
        while num:
            thd = num % 1000
            thousandList = getThousand(thd)
            ans = [ths[thCounts]] + ans if thCounts and thousandList else ans
            ans = thousandList + ans
            num = num // 1000
            thCounts += 1
        return ' '.join(ans)
#================

LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
THOUSANDS = ["", "Thousand", "Million", "Billion"]
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        #check 0
        if not num: return "Zero"
        word = ''
        i = 0
        while num>0:
            if num%1000 != 0:
                word = self.helper(num%1000) + THOUSANDS[i] + " "+ word
            num = num/1000
            i += 1
        return word.strip()
        
    def helper(self, n):
        if n==0:
            return ""
        if n < 20:
            return LESS_THAN_20[n] + " "
        elif n <100:
            return TENS[n/10] +" "+ self.helper(n%10)
        else:
            return LESS_THAN_20[n/100] + " Hundred " + self.helper(n%100)
        
=========yet another way of using python 'and' short circuit for avoiding if clause=====
LT20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
Ts = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
Ks = ["", "Thousand", "Million", "Billion"]

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        word = ""
        i = 0
        while num > 0:
            left = num % 1000
            word = self.helper(left) + Ks[left and i] + " " * (left and 1) + word
            i += 1
            num /= 1000
        return word.strip()
    
    def helper(self, n):
        if n == 0:
            return ""
        if n < 20:
            return LT20[n] + " "
        elif n < 100:
            return Ts[n / 10] + " " + self.helper(n % 10)
        else:
            return LT20[n / 100] + " Hundred " + self.helper(n % 100)
