class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in xrange(32):
            result = result << 1 | n & 1
            n >>= 1
        return result