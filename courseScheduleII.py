#leetcode solution by using dfs and reverse a stack
#also bear in mind internal function like dfs cannot alter the global name hasCycle, it can only refer to global name like ans
#hence the self.hasCycle
#https://leetcode.com/articles/course-schedule-ii/
class Solution(object):
    White = 0
    Gray  = 1
    Black = 2
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.hasCycle = False
        adj = defaultdict(list)
        
        color = [Solution.White for _ in xrange(numCourses)]
        ans = []
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
        
        def dfs(n):
            if self.hasCycle:
                return
            color[n] = Solution.Gray
            if n in adj:
                for nei in adj[n]:
                    if color[nei] == Solution.White:
                        dfs(nei)
                    elif color[nei] == Solution.Gray: #exists cycle
                        self.hasCycle = True
            color[n] = Solution.Black
            ans.append(n)
        
        for n in xrange(numCourses):
            if color[n] == Solution.White:
                dfs(n)
        return ans[::-1] if not self.hasCycle else []
        
