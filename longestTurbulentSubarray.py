#==== 1 dimensional DP array solution====
# array: [9, 4, 2, 10 ,7 ,8 ,8 ,1 ,9]
# trend:  0 -5 -2  +8 -3 +1  0 -7 +8
# maxLth: 1  2  2   3  4  5  1  2  3
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = [[0, 1]] * len(A)
        res = 1
        for i, n in enumerate(A):
            if i == 0:
                continue
            trend = n - A[i-1]
            if trend == 0: # when flat treand happen, reset lth to 1
                maxl = 1
            elif ans[i-1][0] == 0: #when we are at the second from beginning
                maxl = ans[i-1][1] + 1
            elif ans[i-1][0] > 0:
                maxl = ans[i-1][1] + 1 if trend <0 else 2
            elif ans[i-1][0] < 0:
                maxl = ans[i-1][1] + 1 if trend >0 else 2
            ans[i] = (trend, maxl)
            res = max(maxl, res)
        return res
