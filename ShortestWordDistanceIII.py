class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l = len(words)
        dist = l
        i, j = -l, -l
        same = word1 == word2
        for idx in range(l):
            if words[idx] == word1:
                if same:
                    j = i
                    i = idx
                else:
                    i = idx
                dist = min(dist,abs(j-i))
            elif words[idx] == word2:
                j = idx
                dist = min(dist,abs(j-i))
        return dist