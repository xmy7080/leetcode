class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if not s:return [""]
        currset = set()#mark the visited strs, remove duplicates
        from collections import deque
        que = deque()#save the queue
        
        currset.add(s)
        que.append(s)
        
        found = False #found valid str
        while que:
            tmp = que.popleft()
            if self.isvalid(tmp):
                res.append(tmp)
                found = True
        
            if found: continue
            #here we don't need to worry about shorter str got saved in res, because the minus one cut
            #for a valid str, say("()()") must has even paras, since the queue only contains at most one "()" char different strs, all next level strs are with odd paras, which cannot be valid.
        
            for i in xrange(len(tmp)):
                if tmp[i] == '(' or tmp[i] == ')':
                    newstr = tmp[:i]+tmp[i+1:]
                    if newstr not in currset:
                        que.append(newstr)
                        currset.add(newstr)
        return res
        
    def isvalid(self,str):
        count = 0
        for c in str:
            if c == '(':
                count += 1
            elif c == ')':
                if count >0:
                    count -= 1
                else:
                    return False
        return count == 0
        