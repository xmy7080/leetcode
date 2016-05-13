class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
            
        isprime = [True] * n
        isprime[0] = isprime[1] = False
        
        for i in range(2,int (n **0.5) + 1):
            if not isprime[i]: continue
            for j in range(i*i,n,i):
                isprime[j] = False
        count = 0
        for i in range(2,n):
            if isprime[i]: count+=1
        return count
        
        #return sum(isprime)
        
        
