class Solution {
    fun wordBreak(s: String, wordDict: List<String>): List<String> {
        val dict = mutableSetOf<String>()
        for(word in wordDict){
            dict.add(word)
        }
        // println("does cat exists " + dict.contains("cat"))
        val res = mutableListOf<String>()
        val tmp = mutableListOf<String>()
        fun dfs(index: Int){
            if(index == s.length){
                // println("tmp is " + tmp.joinToString("_"))
                res.add(tmp.joinToString(" "))
                return
            }
            for(j in index+1 .. s.length){ // here we need the upper bound as s length, cause the substring function
                val possible = s.substring(index, j)
                if(possible in dict){
                    tmp.add(possible)
                    dfs(j)
                    tmp.removeAt(tmp.size -1)
                }
            }
        }
        dfs(0)
        return res
    }
}
