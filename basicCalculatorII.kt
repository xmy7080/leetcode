//another kotlin way inherited from basic calculator i
class Solution {
    fun calculate(s: String): Long {
        val stk = ArrayDeque<Long>()
        var accu = 0L
        var sign = '+'
        var number = 0L
        println("s last index will read " + s[s.lastIndex]) // in kotlin, lastIndex is 0-based
        for(c in s){
            when (c){
                ' ' -> continue
                '+','-','*','/' -> {
                    when(sign) {
                        '+' -> stk.addFirst(number)
                        '-' -> stk.addFirst(-1 * number)
                        '*' -> stk.addFirst(stk.removeFirst() * number)
                        '/' -> stk.addFirst(stk.removeFirst() / number)
                    }
                    number = 0L
                    sign = c
                }
                else -> number = number * 10 + (c - '0')
            }
        }
        when(sign) { //process the last number when string ends
            '+' -> stk.addFirst(number)
            '-' -> stk.addFirst(-1 * number)
            '*' -> stk.addFirst(stk.removeFirst() * number)
            '/' -> stk.addFirst(stk.removeFirst() / number)
        }
        return stk.sum()
    }
}

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
