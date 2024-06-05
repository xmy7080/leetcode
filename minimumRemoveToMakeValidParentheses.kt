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
