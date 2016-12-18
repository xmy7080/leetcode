from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.l = len(words)
        self.where = defaultdict(list)
        for i in range(len(words)):
            w = words[i]
            self.where[w].append(i)
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.where[word1], self.where[word2]
        min_dist = self.l
        max_ofst = -1
        i, j = 0, 0
        while i<len(l1) and j<len(l2):
            min_dist = min(min_dist, abs(l1[i]-l2[j]))
            if l1[i]>l2[j]:
                j += 1
            else:
                i += 1
        return min_dist
            
        
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")