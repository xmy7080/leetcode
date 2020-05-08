#latest leetcode answer
#pay attention to the counter usage, it could be replaced by a dict, which is parent class of Counter
from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        inCount = Counter({c: 0 for word in words for c in word} )
        #inCount = dict({c: 0 for word in words for c in word} ) will also work
        
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        inCount[b] += 1
                    break
            #check if there are 'abcd', 'ab' for adjacent pairs, cause if a prefix 
            #appears behind a word, there won't be a alphabetic order genereated
            if len(pair[0]) > len(pair[1]) and pair[0].startswith(pair[1]): return ""
        ans = []
        queue = deque([c for c in inCount if inCount[c] == 0])
        while queue:
            c = queue.popleft()
            ans.append(c)
            for ne in adj[c]:
                inCount[ne] -= 1
                if not inCount[ne]:
                    queue.append(ne)
        if len(ans) != len(inCount):
            return "" #contains cycle
        return "".join(ans)
#old leetcode answer
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
