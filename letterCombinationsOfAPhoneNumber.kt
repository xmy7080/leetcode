// traditional dfs solution
class Solution {
    val keyMap: Map<Char,String> = mapOf('2' to "abc", '3' to "def", '4' to "ghi", '5' to "jkl", '6' to "mno", '7' to "pqrs", '8' to "tuv", '9' to "wxyz" )
    fun letterCombinations(digits: String): List<String> {
        val res = mutableListOf<String>()
        fun dfs(temp: StringBuilder, i: Int) {
            var tmp = temp
            if(i == digits.length) {
                res.add(tmp.toString())
                return
            }
            val chars = keyMap[digits[i]] ?: ""
            for (c in chars) {
                tmp = tmp.append(c)
                dfs(tmp, i+1)
                tmp = tmp.deleteCharAt(tmp.length - 1)
            }
        }
        if(digits.length == 0) return res
        dfs(StringBuilder(""), 0)
        return res
    }
}
