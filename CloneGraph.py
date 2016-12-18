# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node: return node
        q = collections.deque()
        q.append(node)
        newhead = UndirectedGraphNode(node.label)
        m = {node:newhead}
        while q:
            tmp = q.popleft()
            for n in tmp.neighbors:
                if n not in m.keys():
                    q.append(n)
                    new = UndirectedGraphNode(n.label)
                    m[n] = new
                    m[tmp].neighbors.append(new)
                else:
                    m[tmp].neighbors.append(m[n])
        return newhead
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #check input
        # if not node: return node
        # q = collections.deque()
        # dic = dict()
        # q.append(node)
        # res = UndirectedGraphNode(node.label)
        # dic[node] = res
        # while q:
        #     n = q.popleft()
        #     for neib in n.neighbors:
        #         if neib not in dic.keys():
        #             tmp = UndirectedGraphNode(neib.label)
        #             dic[neib] = tmp
        #             dic[n].neighbors.append(tmp)
        #             q.append(neib)
        #         else:
        #             tmp = dic[neib]
        #             dic[n].neighbors.append(tmp)
        # return res