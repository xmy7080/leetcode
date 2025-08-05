// editorial solution #2, pay attention to the k = k*10 + (c-'0'), while c.toInt() won't work because it introduced ascii code instead of senmantic number value
class Solution {
    fun decodeString(s: String): String {
        val countStk = Stack<Int>()
        val stringStk = Stack<StringBuilder>()
        var currentStr = StringBuilder("")
        var k = 0
        for(c in s){
            when {
                c.isDigit() -> k = k * 10 + (c - '0')
                c == '[' ->{
                    countStk.push(k)
                    stringStk.push(currentStr)
                    k = 0
                    currentStr = StringBuilder("")
                }
                c == ']' -> {
                    val decodeString = stringStk.pop()
                    val count = countStk.pop()
                    repeat(count) {decodeString.append(currentStr)}
                    currentStr = decodeString
                }
                else -> currentStr.append(c)
            }
        }
        return currentStr.toString()
    }
}
