#geeksforgeeks solution which don't need to go through all possible m in last part

# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity W 
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W]

#jiuzhang solution, will be faster a bit, cause we do check if we are able to put exact size m in backpack
#all impossible sizes we put -1 as a sentinel number. so we need to have a extra go in the bottom to get the answer
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        if not A or not V: return 0
        n = len(A)
        dp = [[-1] * (m+1) for i in xrange(n+1)]
        dp[0][0] = 0
        
        for i in xrange(1, n+1):
            for w in xrange(0, m+1):
                dp[i][w] = dp[i-1][w]
                if w >= A[i-1] and dp[i-1][w - A[i-1]] != -1:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - A[i-1]] + V[i-1])
        
        
        ans = -1
        while m >= 0:
            ans = max(ans, dp[n][m])
            m -= 1
        return ans
