class Solution {
    fun removeDuplicates(s: String): String {
        val stk = Stack<Char>()
        for(c in s){
            if(stk.isNotEmpty() && stk.peek() == c) stk.pop()
            else stk.push(c)
        }
        return stk.joinToString("")
    }
}
