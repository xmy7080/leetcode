class Solution {
    fun maxProfit(prices: IntArray): Int {
        var maxFromRight = prices[prices.size -1]
        var profit = 0
        for(i in prices.size -1 downTo 0){
            maxFromRight = if(prices[i] > maxFromRight) prices[i] else maxFromRight
            if(profit < maxFromRight - prices[i]) profit = maxFromRight - prices[i]
        }
        return profit
    }
}
