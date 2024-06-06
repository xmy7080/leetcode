class Solution {
    fun simplifyPath(path: String): String {
        val strList = path.split("/")
        var stk = mutableListOf<String>()
        strList.forEach {
            when (it){
                "" , "." -> return@forEach
                ".." -> if (stk.size > 0) stk.removeLast()
                else -> stk.add(it)
            }
        }
        return "/" + stk.joinToString("/")
    }
}
