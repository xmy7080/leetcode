#very good explain of the editorial solution
#https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/549233/Breadth-First-Search(BFS)-with-intuitive-approach-Thinking-process
#eitorial solution https://leetcode.com/articles/shortest-path-visiting-all-nodes/
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        que = collections.deque((1 << x, x) for x in xrange(N) )
        dist = collections.defaultdict(lambda: sys.maxint)
        for x in xrange(N): dist[1 << x, x] = 0
        
        while que:
            vis, curr = que.popleft()
            d = dist[vis, curr]
            if vis == 2 ** N -1: return d
            for nei in graph[curr]:
                tmpvis = vis | 1 << nei
                if d+1 < dist[tmpvis, nei]:
                    dist[tmpvis, nei] = d + 1
                    que.append((tmpvis, nei) )
        
