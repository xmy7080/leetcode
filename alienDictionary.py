class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        # find out nodes
        allnodes, Graph, res = set("".join(words)), {}, ""
        for c in allnodes:
            Graph[c] = Node()
        
        # find out directed edges (from StefanPochmann)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if(a != b):
                    Graph[b].IN.add(a)
                    Graph[a].OUT.add(b)
                    break
        
        # topo-sort
        while allnodes:
            oldlen = len(allnodes)
            
            for key in Graph:
                if not Graph[key].IN:    # to remove this
                    for outNode in Graph[key].OUT:
                        Graph[outNode].IN.remove(key)
                    Graph.pop(key, None)
                    res += key
                    allnodes.remove(key)
                    break
            if oldlen == len(allnodes): #if shrinking stops, solution doesn't exist
                return ""
        return res
