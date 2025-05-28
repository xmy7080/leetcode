class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val bools = BooleanArray(s.length+1)
        bools[0] = true
        for(i in 1 .. s.length){
            for(word in wordDict){
                val wordL = word.length
                if( i - wordL >= 0 && s.substring(i - wordL, i) == word && bools[i-wordL]){
                    bools[i] = true
                }
            }
        }
        return bools[s.length]
    }
}
