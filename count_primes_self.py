class Solution(object):
    Primes = [2,3]
    biggestPrime = 3
    def countPrimes(self, n):
        if self.biggestPrime < n:
            for i in range(self.biggestPrime + 2, n, 2):
                if self.isPrime(i):
                    self.Primes.append(i)
            return len(self.Primes)
        else:
            count = 0
            for i in self.Primes:
                if i < n:
                    count += 1
                else:
                    break
            return count
        
    def isPrime(self,n):
        for i in self.Primes:
            if i * i >= n:
                break
            if n % i == 0:
                return False
        return True
