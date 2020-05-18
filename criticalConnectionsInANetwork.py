#inherit from critical router solution
#https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
#https://www.youtube.com/watch?v=jFZsDDB0-vo
#https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation

import sys
sys.setrecursionlimit(10**6)
class Solution:
    def AP(self, n, connects):
        graph = collections.defaultdict(list)
        self.time = 0
        for pair in connects:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        visited = [False] * n
        dscv = [sys.maxint] * n
        low = [sys.maxint] * n
        parent = [-1] * n
        # ap = set()
        ans = []
        def APHelper(u):
            # children = 0
            dscv[u] = self.time
            low[u] = self.time
            visited[u] = True

            self.time += 1
            for v in graph[u]:
                if visited[v] == False:
                    parent[v] = u
                    # children += 1
                    APHelper(v)

                    #update parent low to the lowest low in children
                    low[u] = min(low[u], low[v])

                    # children check is no need here, for remove edge problem, we only care about low and discovery
                    # if parent[u] == -1 and children > 1:
                        # print("ap is " + str(u))
                        # ap.add(u)
                    # if parent[u] != -1 and low[v] >= dscv[u]:
                        # print("ap is " + str(u))
                        # ap.add(u)

                elif v != parent[u]:#when v is visited and not u's parent, update low u to dscv of v
                    low[u] = min(low[u], dscv[v])


        for i in range(n):
            if visited[i] == False:
                APHelper(i)
        print(dscv)
        print(low)
        # print(parent)
        # print(visited)

        for a, b in connects:
            if low[a] > dscv[b] or low[b] > dscv[a]:
                ans.append([a, b] )
        return ans
    
n = 5
connects = [[1, 0], [0, 2], [2, 1], [0,3], [3,4]]
n = 4
connects = [[1, 0], [1, 2], [2, 3]]
n = 7
connects = [[1, 0], [0, 2], [2, 1], [1,3], [1,4], [1,6],[3,5],[4,5]]
   
print "\nArticulation points in first graph "
print(Solution().AP(n, connects) )
