class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        l = len(p)
        count = l
        d = collections.defaultdict(int)
        for c in p:
            d[c] += 1
        for i in xrange(len(s)):
            
            if s[i] in d:#insert first char in substr, do it everytime
                if d[s[i]] >0:
                    count -= 1
                d[s[i]] -= 1
            if i>=l: #remove last char, when the i >= l
                if s[i-l] in d:
                    if d[s[i-l]] >=0:#for "bab" or "bac" targeting "cbb" case, d['b']>=0, count add
                        count += 1
                    #no matter the case is  "bbb" or "bab" targeting "cbb", we add d['b'] by one
                    d[s[i-l]] += 1
            if count == 0:#check if this substr is a anagram
                res.append(i-l+1)
        return res
                 
                
                