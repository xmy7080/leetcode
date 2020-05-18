#video explain https://www.youtube.com/watch?v=jFZsDDB0-vo
#gfg solution https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

import sys
sys.setrecursionlimit(10**6)
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
        self.time = 0
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
        
    def AP(self):
        visited = [False] * self.V
        dscv = [sys.maxint] * self.V
        low = [sys.maxint] * self.V
        parent = [-1] * self.V
        ap = set()
        def APHelper(u):
            children = 0
            dscv[u] = self.time
            low[u] = self.time
            visited[u] = True
            
            self.time += 1
            for v in self.graph[u]:
                if visited[v] == False:
                    parent[v] = u
                    children += 1
                    APHelper(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    if parent[u] == -1 and children > 1:
                        # print("ap is " + str(u))
                        ap.add(u)
                    if parent[u] != -1 and low[v] >= dscv[u]:
                        # print("ap is " + str(u))
                        ap.add(u)
                    
                elif v != parent[u]:#when v is visted and not u's parent, update low u to dscv of v
                    low[u] = min(low[u], dscv[v])
                    
                    
        for i in range(self.V):
            if visited[i] == False:
                APHelper(i)
        print(dscv)
        print(low)
        print(parent)
        print(visited)
        return ap
    
# g3 = Graph (7) 
# g3.addEdge(0, 1) 
# g3.addEdge(1, 2) 
# g3.addEdge(2, 0) 
# g3.addEdge(1, 3) 
# g3.addEdge(1, 4) 
# g3.addEdge(1, 6) 
# g3.addEdge(3, 5) 
# g3.addEdge(4, 5) 
# print "\nArticulation points in third graph "
# print(g3.AP() )

# g2 = Graph(4) 
# g2.addEdge(0, 1) 
# g2.addEdge(1, 2) 
# g2.addEdge(2, 3) 
# print "\nArticulation points in second graph "
# print(g2.AP() )
# Create a graph given in the above diagram 
g1 = Graph(5) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(2, 1) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4) 
   
print "\nArticulation points in first graph "
print(g1.AP() )
