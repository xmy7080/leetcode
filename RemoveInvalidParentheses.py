class Solution(object):
    minRem = None
    res = None
    
    def reset(self):
        self.minRem = float("inf")
        self.res = set()
        
    def dfs(self, idx, string, l, r, tmp, minRem):
        if idx == len(string):
            if l == r:
                if minRem <= self.minRem:
                    
                    str = "".join(tmp)
                    if minRem < self.minRem:
                        self.res = set()
                        self.minRem = minRem
                    self.res.add(str)
        else:
            curr = string[idx]
            if curr != '(' and curr != ')':
                tmp.append(curr)
                self.dfs(idx+1, string, l, r, tmp, minRem)
                tmp.pop()
            else:
                self.dfs(idx+1, string, l, r, tmp, minRem+1)
                if curr == '(':
                    tmp.append(curr)
                    self.dfs(idx+1, string, l+1, r, tmp, minRem)
                    tmp.pop()
                elif l > r:
                    tmp.append(curr)
                    self.dfs(idx+1, string, l, r+1, tmp, minRem)
                    tmp.pop()
                
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.reset()
        self.dfs(0, s, 0, 0, [], 0)
        return list(self.res)
        
# class Solution(object):
#     def removeInvalidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         res = []
#         if not s:return [""]
#         currset = set()#mark the visited strs, remove duplicates
#         from collections import deque
#         que = deque()#save the queue
        
#         currset.add(s)
#         que.append(s)
        
#         found = False #found valid str
#         while que:
#             tmp = que.popleft()
#             if self.isvalid(tmp):
#                 res.append(tmp)
#                 found = True
        
#             if found: continue
#             #here we don't need to worry about shorter str got saved in res, because the minus one cut
#             #for a valid str, say("()()") must has even paras, since the queue only contains at most one "()" char different strs, all next level strs are with odd paras, which cannot be valid.
        
#             for i in xrange(len(tmp)):
#                 if tmp[i] == '(' or tmp[i] == ')':
#                     newstr = tmp[:i]+tmp[i+1:]
#                     if newstr not in currset:
#                         que.append(newstr)
#                         currset.add(newstr)
#         return res
        
#     def isvalid(self,str):
#         count = 0
#         for c in str:
#             if c == '(':
#                 count += 1
#             elif c == ')':
#                 if count >0:
#                     count -= 1
#                 else:
#                     return False
#         return count == 0
        
