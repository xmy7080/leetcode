#python dijkstra solution using heapq
#https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        q, dic, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w) )
        while q:
            time, curr = heappop(q)
            if curr not in dic:
                dic[curr] = time
                for v, w in adj[curr]:
                    heappush(q, (time+ w, v) )
        return max(dic.values() ) if len(dic) == N else -1
