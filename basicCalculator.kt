//asked during navan phone screen
//solution from https://leetcode.com/problems/basic-calculator/solutions/2831536/understandable-solution/

class Solution {
    fun calculate(s: String): Long {
        var stk = ArrayDeque<Long>()
        var sign = 1L
        var accu = 0L
        var currNum = 0L
        for (c in s) {
            when (c) {
            ' ' -> continue
            '+','-' -> {
                accu += sign * currNum
                // print("currNum is " + sign * currNum)
                // println(" accu is " + accu)
                currNum = 0
                sign = if (c == '+') 1 else -1
            }
            '(' -> {
                stk.addFirst(accu)
                stk.addFirst(sign)
                accu = 0 // reset the accu before going in bracket
                sign = 1 // reset the sign before going in bracket
            }
            ')' -> {
                accu += sign * currNum // sum within the bracket
                // print("currNum is " + sign * currNum)
                accu *= stk.removeFirst() // times the sign before this bracket start
                // print(" accu witin bracket is " + accu)
                accu = stk.removeFirst()/* accu before this bracket */ + accu // the result before this bracket start add the final bracketSum
                // println(" accu out of bracket is " + accu)
                currNum = 0
            }
            else -> currNum = currNum * 10 + (c - '0')
            }
        }
        accu += sign * currNum
        // print("currNum is " + sign * currNum)
        // println(" accu is " + accu)
        return accu
    }
}
/*
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
 s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.


Input: s = "10 + 2”
Output: 12

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
( -> stack in
) -> pop stack until we saw another (
(1+(4+5+2)-3) //( accu = 1
//( 1  +// accu = 0 
  ")" -> // // 1 + accu
 */
