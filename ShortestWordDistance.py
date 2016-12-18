class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1, i2 = -1, -1
        dist = len(words)
        for i in range(len(words)):
            if word1 == words[i]:
                i1 = i
            elif word2 == words[i]:
                i2 = i
            if i1!=-1 and i2!=-1: 
                dist = min(dist,abs(i2-i1))
                if dist == 1: break
        return dist