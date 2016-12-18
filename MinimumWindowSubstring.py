class Solution(object):
    # def minWindow(self, s, t):
    #     m = len(s)
    #     n = len(t)
    #     if m < n:
    #         return ''
    #     lt = {}
    #     for i in t:
    #         if i not in lt:
    #             lt[i] = 1
    #         else:
    #             lt[i] += 1
    #     missing = n
    #     i = I = J = 0
    #     for j, c in enumerate(s, 1):    
    #         if c in lt and lt[c] > 0:
    #             missing -= 1
    #         if c in lt:
    #             lt[c] -= 1

    #         while i < j and not missing:
    #             if not J or j-i < J-I:
    #                 I, J = i, j
    #             if s[i] not in lt:
    #                 i += 1
    #                 continue
    #             else:
    #                 lt[s[i]] += 1
    #                 if lt[s[i]] > 0:
    #                     missing += 1
    #                 i += 1
    #     return s[I:J]
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        missing, dic = len(t), collections.defaultdict(int)
        if len(t) > len(s):
            return ''
        for c in t:
            dic[c] += 1
        
        i = I = J = 0 #first assigned I,J to 0 because we are not sure we can find the cover
        for j, c in enumerate(s,1):
            if c in dic:
                if dic[c] > 0:
                    missing -= 1
                dic[c] -= 1
                
            # while i < j and not missing:
            #     if not J or j-i < J-I:
            #         I, J = i, j
            #     if s[i] not in dic:
            #         i += 1
            #         continue
            #     else:
            #         dic[s[i]] += 1
            #         if dic[s[i]] > 0:
            #             missing += 1
            #         i += 1
            
            while not missing:#missing = 0, when s[i:j] has covered all t chars
                # if s[i] not in dic:#deal with chars not in str t
                #     i += 1
                #     continue
                if s[i] in dic:
                    dic[s[i]] += 1
                    if dic[s[i]] > 0:#when any of char in t has turn positive, s[i:j] is not suffice
                        missing += 1#add missing to positive, leave the loop on next round
                if not J or j-i < J-I:#when found the covered part, update I J when J are not assigned anything yet, OR, when found shorter part
                    I, J = i, j
                i += 1 #no matter it's in dic, we finish this s[i] and made i++
        return s[I:J]
        
        
        
        
        
        
        
        
        
        
        
        
        
        #this is a rewrite of 12 lines python code which used counters, this solution use defaultdict
        #as well
        # import collections
        # need, missing = collections.defaultdict(int), len(t)
        # for c in t:
        #     need[c] += 1
        # i = I = J = 0
        # for j, c in enumerate(s,1):
        #     if need[c] >0:
        #         missing -= 1
        #     need[c] -= 1
        #     if not missing:
        #         while i<j and not( s[i] in need and need[s[i]] >= 0 ):
        #             if s[i] in need:
        #                 need[s[i]] += 1
        #             i += 1
        #         if not J or j-i <= J-I:
        #             I, J = i, j
        # return s[I:J]