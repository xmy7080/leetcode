// a more understandable solution without the lambda build string
class Solution {
    fun minRemoveToMakeValid(s: String): String {
        val sb = StringBuilder("")
        val stk = Stack<Int>()
        for(i in 0 until s.length){
            when (s[i]){
                '(' -> stk.push(sb.length)
                ')' -> if(stk.isNotEmpty()) stk.pop()
                    else continue
            }
            sb.append(s[i])
        }
        // println("sb is ${sb.toString()}")
        stk.reversed().forEach{
            sb.deleteAt(it)
        }
        return sb.toString()
    }
}

// this solution is using the kotlin buildString function. 
//buildString in Kotlin is an inline function that provides an efficient way to construct strings using a StringBuilder. 
//It takes a lambda expression as an argument, within which you can append or manipulate the string. The function then returns the final constructed string. 
//
//fun buildString(builderAction: (StringBuilder) -> Unit): String

/*
val result = buildString {
    append("Hello, ")
    append("World!")
}
println(result) // Output: Hello, World!
*/
class Solution {
    fun minRemoveToMakeValid(s: String)= buildString {
        var stk = mutableListOf<Int>()
        for (c in s) {
            when (c) {
                '(' -> stk.add(length)
                ')' -> if (stk.isNotEmpty()) stk.removeLast()
                        else continue
            }
            append(c)
        }
        for (i in stk.size-1 downTo 0){
            deleteAt(stk[i])
        }
    }
}

// Original solution, takes too long to run
    // fun minRemoveToMakeValid(s: String): String {
    //     var stk = ArrayDeque<Int>()
    //     var rmv = HashSet<Int>()
    //     var charArray = s.toCharArray()
    //     charArray.forEachIndexed { idx, char ->
    //         if (char !in listOf ('(', ')') )
    //             return@forEachIndexed
    //         else if (char == '(')
    //             stk.addFirst(idx)
    //         else if (stk.size == 0)
    //             rmv.add(idx)
    //         else
    //             stk.removeFirst()
    //     }
    //     rmv += HashSet(stk)
    //     var result = charArrayOf()
    //     charArray.forEachIndexed { idx, char ->
    //         if (idx !in rmv)
    //             result += char
    //     }
    //     return result.joinToString("")
    // }


// another more kotlin taste solution
// class Solution {
//     fun minRemoveToMakeValid(s: String) = buildString {
//         val indexes = mutableListOf<Int>()
//         s.forEach {
//             when (it) {
//                 '(' -> indexes.add(length)
//                 ')' -> if (!indexes.isEmpty()) indexes.removeLast()
//                        else return@forEach
//             }
//             append(it)
//         }
//         indexes.reversed().forEach {
//             deleteAt(it)
//         }
//     }
// }
