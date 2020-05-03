#leetcode solution used a marked color dictionary, which used less memory
#https://leetcode.com/articles/is-graph-bipartite/
#my solution use two sets and two queues and bfs traverse, which is working but used a little more space
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        size = len(graph)
        visited = [False] * size
        for vert in xrange(size):
            if visited[vert]:
                continue
            currSet = set([vert])
            currQue = deque([vert])
            nextSet = set()
            nextQue = deque()
            while currQue:
                node = currQue.popleft()
                for ne in graph[node]:
                    if ne in currSet:
                        return False
                    else:
                        if not visited[ne] and ne not in nextSet:
                            nextSet.add(ne)
                            nextQue.append(ne)
                visited[node] = True

                if not currQue:
                    tmpSet = currSet
                    currSet = nextSet
                    currQue = nextQue
                    nextSet = tmpSet
                    nextQue = deque()
        # print(currSet)
        # print(nextSet)
        
        return True
