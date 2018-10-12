class Solution(object):
    def ip2number(self, ip):
        num = list(map(int, ip.split('.')))
        return (num[0]<<24) + (num[1]<<16) + (num[2]<<8) + num[3]
    
    def number2ip(self, number):
        return str(number>>24 & 255) + '.' + str(number>>16 & 255) + '.' + str(number>>8 & 255) + '.' + str(number & 255)
        
    def lowestBit(self, x):
        for i in xrange(32):
            if(x & (1<<i)):
                return i
    def lowestBitValue(self, x):
        return 1 << self.lowestBit(x)
    
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        number = self.ip2number(ip)
        res = []
        while n > 0:
            lowBitVal = self.lowestBitValue(number)
            while lowBitVal > n:
                lowBitVal = lowBitVal / 2
            n = n-lowBitVal
            res.append(str(self.number2ip(number) + '/' + str(32 - self.lowestBit(lowBitVal) )))
            number += lowBitVal
        return res
        # return [ (self.number2ip(self.ip2number(ip) + 255*255)) ]
        # check if number2ip and ip2number function works.
        
        
