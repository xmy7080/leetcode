class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        val res = strs[0].toCharArray()
        for (i in 0 until strs[0].length){
            strs.forEach{

                if(i >= it.length || it[i] != res[i]) return res.take(i).joinToString("")
            }
        }
        return res.joinToString("")
    }
}
