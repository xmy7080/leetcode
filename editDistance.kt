class Solution {
// approach using mXn matrix
    fun minDistance(word1: String, word2: String): Int {
        val m = word1.length
        val n = word2.length
        val res = Array(m+1) { IntArray(n+1) {0}}
        for(i in 0 .. m){
            for(j in 0 .. n){
                // distance for empty a to non-empty b
                if(i == 0) res[i][j] = j
                // distance for non-empty a to empty b
                else if(j == 0) res[i][j] = i
                else {
                    //                   replace last char, add last char to a, delete last char from a
                    res[i][j] = intArrayOf(res[i-1][j-1] + 1, res[i][j-1] + 1, res[i-1][j] + 1).min()
                    // when last char of a == last char of b
                    if(word1[i-1] == word2[j-1]) res[i][j] = intArrayOf(res[i][j], res[i-1][j-1]).min()
                }
            }
        }
        return res[m][n]
    }
}
