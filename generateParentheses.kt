class Solution {
    fun generateParenthesis(n: Int): List<String> {
        val sb = StringBuilder("")
        val res = mutableListOf<String>()
        fun helper(left: Int, right: Int){
            if(sb.length == 2* n) res.add(sb.toString())
            if(left < n) {
                sb.append("(")
                helper(left + 1, right)
                sb.deleteAt(sb.length -1)
            }
            if (left > right){
                sb.append(")")
                helper(left, right + 1)
                sb.deleteAt(sb.length -1)
            }
        }
        helper(0, 0)
        return res
    }
}
