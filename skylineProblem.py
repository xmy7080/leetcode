#https://leetcode.com/problems/the-skyline-problem/discuss/61210/14-line-python-code-straightforward-and-easy-to-understand
#above solution use min heap to get the height of curr top
#be aware that set.sort() is illegal, has to do smth = sorted(set())
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def addSky(pos, high):
            if ans[-1][1] != high:
                ans.append([pos, high])
        position = set([ b[0] for b in buildings ] + [b[1] for b in buildings ])
        
        live = []
        ans = [[-1,0] ] #initialize ans, cause addSky need to check last item in the addSky
        allPosi = sorted(position)
        i = 0
        for p in allPosi:
            # add the new buildings whose left side is lefter than position t
            while i < len(buildings) and buildings[i][0] <= p:
                heappush(live, (-buildings[i][2], buildings[i][1]) )
                i += 1
                
            # remove the past buildings whose right side is lefter than position t
            while live and live[0][1] <= p:
                heappop(live)
                
            # pick the highest existing building at this moment
            high = -live[0][0] if live else 0
            addSky(p, high)
        return ans[1:]
