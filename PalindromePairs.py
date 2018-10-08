class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(s):
            return s == s[::-1]
        
        words = {word: i for i, word in enumerate(words)}
        res = []
        for word, k in words.iteritems():
            n = len(word)
            for j in xrange(n+1):
                prefix = word[:j]
                suffix = word[j:]
                if isPalindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in words:
                        res.append([words[back], k])
                if j != n and isPalindrome(suffix):
                    back = prefix[::-1]
                    if back is not word and  back in words:
                        res.append([k, words[back]])
        return res
    
