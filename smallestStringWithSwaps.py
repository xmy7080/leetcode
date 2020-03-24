#==byteDance company frequent problems, first problem with union find
#basically, [0,1,2,3,4] is indicating a all separate union set, when there are unit operation, we point self.p[x] = self.find(y)
# then after unit(0,2) it become [2,1,2,3,4], after unit(2,3) it become [2,1,3,3,4]
#finally when we do self.find(0), it will update self.p[0] to its origin 3, array become [3,1,3,3,4] and return the right origin
#https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        class UF:
            def __init__(self, n): self.p = range(n)
            def unit(self, x, y): self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if self.p[x] != x: self.p[x] = self.find(self.p[x])
                return self.p[x]
        uf, ans, dic = UF(len(s)), [], defaultdict(list)
        for a, b in pairs:
            uf.unit(a, b)
        for i in xrange(len(s)):
            dic[uf.find(i)].append(s[i])
        for key in dic:
            dic[key].sort(reverse = True)
        for i in xrange(len(s)):
            ans.append(dic[uf.find(i)].pop())
        return ''.join(ans)
