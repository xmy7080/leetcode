class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(n, i, combi,combis):
            while i*i <= n:
                if n%i == 0:
                    combis.append(combi + [i, n/i])
                    dfs(n/i, i, combi + [i], combis)
                i += 1
            return combis
        return dfs(n, 2, [],[])