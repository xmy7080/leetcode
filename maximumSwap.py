#===solution on the second greedy way https://leetcode.com/articles/maximum-swap/
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = map(int, str(num)) #3455 => [3,4,5,5]
        last = {x: i for i, x in enumerate(A)} #{3: 0, 4:1, 5:3}
        for i, n in enumerate(A):
            for nextBig in xrange(9, n, -1):
                if last.get(nextBig, None) > i:
                    A[i], A[last[nextBig]] = A[last[nextBig]], A[i]
                    return int("".join(map(str, A)))
        return num
