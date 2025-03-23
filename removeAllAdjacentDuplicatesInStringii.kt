// use the native stack class of kotlin
// use the repeat(k){action function}
// remember not to use the data class when define object that can have duplicate
class Solution {
    class LetterCount(val letter: Char, val count: Int)
    fun removeDuplicates(s: String, k: Int): String {
        val stk = Stack<LetterCount>()
        s.forEach{c ->
            val count = if(stk.isNotEmpty() && stk.peek().letter == c ) stk.peek().count + 1 else 1
            stk.push(LetterCount(c, count))
            if(count == k) repeat(k){stk.pop()}
        }
        return stk.map{it.letter}.joinToString("")
    }
}
