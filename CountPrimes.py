class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        notprime = [False]*n
        for i in xrange(2,n):
            if not notprime[i]:
                count += 1
                j = i*i
                while j < n:
                    notprime[j] = True
                    j+=i
        return count            
        
        