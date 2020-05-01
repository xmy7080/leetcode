#leetcode solution #2
#be aware of the iter usage, next(iter) and next(iter,None)
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        heads = [[] for _ in xrange(26)]
        ans = 0
        for w in words:
            it = iter(w)
            heads[ord(next(it)) - ord('a') ].append(it)
        for s in S:
            letter = ord(s) - ord('a')
            oldBucket = heads[letter]
            heads[letter] = []
            for it in oldBucket:
                 # = oldBucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1
        return ans
