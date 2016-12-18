class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            l = list(s)
            l.sort()
            key = ''.join(l)
            d[key] = d.get(key,[]) + [s]
        return list(d.values())
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # d = {}
        # for str in strs:
        #     l = list(str)
        #     l.sort()
        #     key = ''.join(l)
        #     d[key] = d.get(key,[]) + [str]
        # return list(d.values())
        