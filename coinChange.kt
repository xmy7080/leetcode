class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        // var biggestCoin = coins.maxOrNull() ?: 0
        // because coins can contain an over 2B integer, we can't initiate a int array by the biggest coin, while in reality this may make more sense
        // instead, because the amount can be as big as 10^4, we can initiate int array by the size of the amount
        var biggestCoin = coins.maxOrNull() ?: 0
        // val numberOfCoins = IntArray(biggestCoin){-1}
        val numberOfCoins = IntArray(amount+1){-1}
        numberOfCoins[0] = 0
        for(i in 1 .. amount){
            var lowestNumber = Int.MAX_VALUE
            for(coin in coins){
                // val position = (i - coin) % biggestCoin
                val position = i - coin
                if( position >= 0 && numberOfCoins[position] != -1 ){
                    if(lowestNumber > numberOfCoins[position] + 1) 
                        lowestNumber = numberOfCoins[position] + 1
                }
            }
            // numberOfCoins[i % biggestCoin] = if(lowestNumber != Int.MAX_VALUE) lowestNumber else -1
            numberOfCoins[i] = if(lowestNumber != Int.MAX_VALUE) lowestNumber else -1
        }
        // return numberOfCoins[amount % biggestCoin]
        return numberOfCoins[amount]
    }
}
