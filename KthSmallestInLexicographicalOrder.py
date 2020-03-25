#https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/92242/ConciseEasy-to-understand-Java-5ms-solution-with-Explaination
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        curr = 1
        k = k-1
        while k > 0:
            steps = self.calSteps(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1 # 1 step down the tree, eg 1 -> 10, 11 -> 110
        return curr
    
    def calSteps(self, t, n1, n2):
        steps = 0
        while n1 <= t: #when n1 = 1 or 10 and t = 13
            steps += min(t +1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps
