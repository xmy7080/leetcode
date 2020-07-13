#lt solution, second one of the greedy
from heapq import heapify, heappush, heappop
class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapify(pq)
        a, v = pq[0]
        if -a > (len(S) +1)/2 :
            return ""
        
        ans = []
        while len(pq) >1:
            ct1, c1 = heappop(pq)
            ct2, c2 = heappop(pq)
            if ans and c1 == ans[-1]:
                ans += [c2, c1]
            else:
                ans += [c1, c2]
                
            #pay attention ct1 is always < 0, hence need push back ct1 + 1/ct2 + 1
            if ct1 + 1: heappush(pq, (ct1 + 1, c1))
            if ct2 + 1: heappush(pq, (ct2 + 1, c2))
        return "".join(ans) + (pq[0][1] if pq else "")
