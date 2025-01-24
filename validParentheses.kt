class Solution {
    fun isValid(s: String): Boolean {
        val stk = ArrayDeque<Char>()
        s.forEach{
            when (it) {
                '(','[','{' -> stk.addFirst(it)
                ')' -> if(stk.firstOrNull() != '(') return false else stk.removeFirst()
                ']' -> if(stk.firstOrNull() != '[') return false else stk.removeFirst()
                '}' -> if(stk.firstOrNull() != '{') return false else stk.removeFirst()
                // else -> 
            }
        }
        return stk.isEmpty()
    }
}
