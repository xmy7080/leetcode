class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        candidates.sort()
        self.dfs(res,tmp,0,candidates,target)
        return res if target else []
        
    def dfs(self,res,tmp,start,cand,target):
        if target == 0:
            ele = list(tmp)
            res.append(ele)
            return
        for i in range(start,len(cand)):
            if target < cand[i]:
                return
            tmp.append(cand[i])
            self.dfs(res,tmp,i,cand,target-cand[i])
            tmp.pop()