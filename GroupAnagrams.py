#faster way of put counts as a tuple in the dic key
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a') ] += 1
            dic[tuple(count) ].append(str)
        return dic.values()
    
#original way or sorting the strings
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
        
