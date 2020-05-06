#given n = 5 the 
##output ['11011', '11010', '11001', '10110', '10101', '10100', '10011', '10010', '01101', '01100', '01011', '01010', '01001', '00110', '00101', '00100']
#"11100" or "10001" isn't the valid answer
class Solution(object):
    def generate01(self, n):
        """
        :type n: int
        :rtype: [string]
        """
        ans = []
        def dfs(i, accu, tmpstr):
            if i == n and accu < 3:
                ans.append(tmpstr)
                return
            if accu == 2:
                tmpstr += str(1- int(tmpstr[i-1]) )
                dfs(i+1, 1, tmpstr)
                tmpstr = tmpstr[:-1]
            else:
                tmpstr += '1'
                newaccu = accu + 1 if tmpstr[i-1] == '1' else 1
                dfs(i+1, newaccu, tmpstr)
                tmpstr = tmpstr[:-1]
                
                tmpstr += '0'
                newaccu = accu + 1 if tmpstr[i-1] == '0' else 1
                dfs(i+1, newaccu, tmpstr)
                tmpstr = tmpstr[:-1]
                
                
        dfs(0, 0, "")
        return ans

print(Solution().generate01(5))
