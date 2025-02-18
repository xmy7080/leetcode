// traditional dfs solution
class Solution {
    val keyMap: Map<Char,String> = mapOf('2' to "abc", '3' to "def", '4' to "ghi", '5' to "jkl", '6' to "mno", '7' to "pqrs", '8' to "tuv", '9' to "wxyz" )
    fun letterCombinations(digits: String): List<String> {
        val res = mutableListOf<String>()
        fun dfs(tmp: StringBuilder, i: Int) {
            // var tmp = temp
            if(i == digits.length) {
                res.add(tmp.toString())
                return
            }
            val chars = keyMap[digits[i]] ?: ""
            for (c in chars) {
                tmp.append(c) // used to be tmp = tmp.append(c), but turns out append will just change string builder object directly
                dfs(tmp, i+1)
                tmp.deleteCharAt(tmp.length - 1) // used to be tmp = tmp.deleteCharAt(), same reason with above
            }
        }
        if(digits.length == 0) return res
        dfs(StringBuilder(""), 0)
        return res
    }
}
