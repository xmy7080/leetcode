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
