// solution from the editorial
// https://leetcode.com/problems/basic-calculator-iii/
// september 12 work, pretty much the same. Also inherited from calculator II
class Solution {
    fun calculate(s: String): Int {
        val stk = ArrayDeque<String>()
        var accu = 0
        var sign = '+'
        var number = 0
        val str = s + "@"
        for (c in str){
            if (c.isDigit()) {
                number = number * 10 + (c - '0')
            } else if (c == '('){
                // stk.addFirst(number.toString())
                stk.addFirst(sign.toString())
                sign = '+'
            } else {
                when (sign) {
                    '+' -> stk.addFirst( number.toString())
                    '-' -> stk.addFirst( (-1 * number).toString())
                    '*' -> stk.addFirst( (stk.removeFirst().toInt() * number).toString() )
                    '/' -> stk.addFirst( (stk.removeFirst().toInt() / number).toString() )
                }
                number = 0
                sign = c
                if (c == ')') {
                    while (stk.first() !in listOf("+", "-", "*", "/")){
                        number += stk.removeFirst().toInt()
                    }
                    sign = stk.removeFirst().single()
                }
            }
        }
        // println("stk is " + stk.joinToString(","))
        return stk.map{it.toInt()}.sum()
    }
}

//=======
class Solution {
    fun calculate(s: String): Int {
        val stk = ArrayDeque<String>()
        var digit = 0
        var lastSign = "+"
        var str: String = s + "@"

        for (c in str){
            if (c.isDigit()){
                digit = digit * 10 + c.toInt() - '0'.toInt()
            } 
            else if (c == '('){
                stk.addFirst(lastSign)
                lastSign = "+"
            }
            else {
                when (lastSign){
                    "+" -> stk.addFirst( digit.toString() )
                    "-" -> stk.addFirst( (-1 * digit).toString() )
                    "*" -> stk.addFirst( (stk.removeFirst().toInt() * digit).toString() )
                    "/" -> stk.addFirst( (stk.removeFirst().toInt() / digit).toString() )
                }
                lastSign = c.toString()
                digit = 0
                if (c ==')'){
                    // println("stk is " + stk.reversed().joinToString(","))
                    while (stk.first() !in hashSetOf<String>("+", "-", "*", "/")){
                        digit += stk.removeFirst().toInt()
                    }
                    lastSign = stk.removeFirst()
                }
            }
            
        }
        // println("stk is " + stk.joinToString(","))
        return stk.map{it.toInt()}.sum()
    }
}
