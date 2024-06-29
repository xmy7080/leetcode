// kotlin way of my original python solution
// https://leetcode.com/problems/basic-calculator-ii/solutions/3465561/kotlin-way/
class Solution {
    fun calculate(s: String): Int {
        val stk = ArrayDeque<Int>()
        var digit = 0
        var prevSign = '+'

        for (i in 0..s.lastIndex){
            val char: Char = s[i]
            if (char.isDigit()){
                digit = digit * 10 + char.toInt() - '0'.toInt()
            }
            if (char in hashSetOf<Char>('+', '-', '*', '/') || i == s.lastIndex){
                when (prevSign){
                    '+' -> stk.addFirst(digit)
                    '-' -> stk.addFirst(-digit)
                    '*' -> stk.addFirst(stk.removeFirst() * digit )
                    '/' -> stk.addFirst(stk.removeFirst() / digit )
                }
                prevSign = char
                digit = 0
            }
        }
        return stk.sum()
    }
}
